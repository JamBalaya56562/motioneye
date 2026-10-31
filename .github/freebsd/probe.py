"""Probe what motionEye does on FreeBSD: the platform helpers, then a server with one
network camera driven like the web UI. Prints findings; never fails the job."""

from __future__ import annotations

import logging
import subprocess
import sys
import time
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tests'))
from hub_remote_compat import Client  # noqa: E402

PORT = 18765
MOTION_PORT = 17999
PICTURE_PORT = 18090
PASSWORD = 'freebsd-probe'


def section(title: str) -> None:
    print(f'\n===== {title}', flush=True)


def probe(label: str, func) -> None:
    try:
        print(f'{label}: {func()!r}', flush=True)
    except Exception:
        print(f'{label}: RAISED', flush=True)
        traceback.print_exc(file=sys.stdout)


def shell(cmd: str) -> None:
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(f'$ {cmd} -> {result.returncode}\n{result.stdout}{result.stderr}', flush=True)


def helpers() -> None:
    section('platform helpers')
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, format='  log %(levelname)s %(message)s')
    from motioneye import motionctl, update
    from motioneye.controls import diskctl, smbctl, v4l2ctl

    probe('update.get_os_version', update.get_os_version)
    probe('motionctl.find_motion', motionctl.find_motion)
    probe('v4l2ctl.find_v4l2_ctl', v4l2ctl.find_v4l2_ctl)
    probe('diskctl.list_mounted_disks', diskctl.list_mounted_disks)
    probe('diskctl.list_mounted_partitions', diskctl.list_mounted_partitions)
    probe('smbctl.find_mount_cifs', smbctl.find_mount_cifs)
    probe('smbctl.list_mounts', smbctl.list_mounts)
    for cmd in ('mount -p', 'gpart show', 'geom disk list | head -20', 'ls /dev/disk 2>&1', 'fdisk -l 2>&1 | head',
                'which sha1sum lsb_release v4l2-ctl mount.cifs mount_smbfs poweroff shutdown systemctl curl'):
        shell(cmd)
    logging.getLogger().handlers.clear()


def server(venv: Path, root: Path) -> None:
    section('server')
    for d in ('run', 'log', 'media', 'pictures'):
        (root / d).mkdir(parents=True, exist_ok=True)
    from PIL import Image
    from argon2 import PasswordHasher

    Image.new('RGB', (640, 480), (40, 90, 140)).save(root / 'pictures' / 'cam.jpg', 'JPEG')

    def write(name: str, *lines: str) -> None:
        (root / name).write_text('\n'.join(lines) + '\n')

    write('motioneye.conf', f'conf_path {root}', f'run_path {root / "run"}', f'log_path {root / "log"}',
          f'media_path {root / "media"}', f'port {PORT}', 'listen 127.0.0.1',
          f'motion_control_port {MOTION_PORT}', 'log_level debug')
    password_hash = PasswordHasher().hash(PASSWORD)
    write('motion.conf', 'setup_mode off', f'# @admin_password {password_hash}',
          f'# @normal_password {password_hash}', 'camera camera-1.conf')
    write('camera-1.conf', '# @id 1', '# @enabled on', '# @proto netcam', 'camera_name Probe',
          f'netcam_url http://127.0.0.1:{PICTURE_PORT}/cam.jpg', f'target_dir {root / "media" / "Probe"}',
          'framerate 2', 'stream_maxrate 2', 'snapshot_interval 0')

    pictures = subprocess.Popen([sys.executable, '-m', 'http.server', str(PICTURE_PORT), '--bind', '127.0.0.1'],
                                cwd=root / 'pictures', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log = (root / 'server.log').open('w')
    meye = subprocess.Popen([str(venv / 'bin' / 'meyectl'), 'startserver', '-c', str(root / 'motioneye.conf'), '-l'],
                            cwd=root, stdout=log, stderr=subprocess.STDOUT)
    try:
        import hub_remote_compat

        hub_remote_compat.ADMIN_PASSWORD = PASSWORD  # read by Client.login()
        client = Client(PORT)
        deadline = time.monotonic() + 90
        while True:
            try:
                client.request('GET', '/')
                break
            except OSError:
                if time.monotonic() > deadline:
                    raise
                time.sleep(1)
        print('server answers', flush=True)
        probe('login', client.login)
        probe('/config/list/', lambda: [c.get('name') for c in client.get_json('/config/list/')['cameras']])
        answer = client.get_json('/config/1/get/')
        print('available_disks:', answer.get('available_disks'), flush=True)
        print('storage_device:', answer.get('storage_device'), flush=True)
        probe('save the camera as the UI does', lambda: client.post_json('/config/1/set/', answer))
        time.sleep(15)
        shell('pgrep -lf "motion -n"')
        shell(f'grep -E "^on_" {root}/camera-1.conf')
        probe('/action/1/eventstart', lambda: client.post_json('/action/1/eventstart/', {}))
        time.sleep(5)
        shell(f'sh -x {venv}/lib/python3*/site-packages/motioneye/scripts/relayevent.sh {root}/motioneye.conf start 1; echo exit $?')
        probe('/action/1/snapshot', lambda: client.post_json('/action/1/snapshot/', {}))
        time.sleep(5)
        shell(f'find {root}/media -type f | head')
        status, ctype, data = client.request('GET', '/picture/1/current/')
        print(f'/picture/1/current/: {status} {ctype} {len(data)} bytes', flush=True)
        status, ctype, data = client.request('GET', '/config/backup/')
        print(f'/config/backup/: {status} {ctype} {len(data)} bytes', flush=True)
    except Exception:
        traceback.print_exc(file=sys.stdout)
    finally:
        meye.terminate()
        meye.wait(30)
        shell('pkill -f "motion -n"')
        pictures.terminate()
        log.close()

    section('server log: warnings, errors, relay, motion')
    lines = (root / 'server.log').read_text(errors='replace').splitlines()
    keep = [line for line in lines if any(k in line for k in ('WARNING', 'ERROR', 'Traceback', 'Error', 'relay',
                                                                '_relay_event', 'motion detected', 'hello'))]
    print('\n'.join(keep[:200]) or '(nothing)', flush=True)
    section('motion log tail')
    shell(f'tail -40 {root}/log/motion.log 2>&1')


if __name__ == '__main__':
    venv, root = Path(sys.argv[1]), Path(sys.argv[2])
    helpers()
    server(venv, root)
