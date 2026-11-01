# FreeBSD support (`enh/freebsd`, takes over #1616, closes #2610)

This note keeps the investigation results so review questions can be answered right away. **Checking anything again on a VM takes about an hour per run** (vmactions/freebsd-vm; installing from pip is slow, and PyPI timed out more than once), so record what is already settled here.

- Branch: `JamBalaya56562:enh/freebsd` (`299fa7aa`, on dev `f75a18aa`). Not submitted (we already have two open PRs, #3506 and #3507)
- PR body: [pr-drafts.md](pr-drafts.md)
- Co-authors: ascl00 (author of #1616), paulprocacci (#2610, who asked for the rc script)
- Each claim is labelled with the kind of evidence: **検証済み / ドキュメント根拠 / コード根拠 / 推測 / 未検証**

## Verification runs (fork's Actions)

| Run | Branch / commit | What it checked |
|---|---|---|
| [41246187587](https://github.com/JamBalaya56562/motioneye/actions/runs/41246187587), [41252232495](https://github.com/JamBalaya56562/motioneye/actions/runs/41252232495) | `repro/freebsd` `13e01a0b` / `1ad534d1` | State of dev on 14.3 / 15.1 (what works, what is broken) |
| [41275336079](https://github.com/JamBalaya56562/motioneye/actions/runs/41275336079) | `repro/freebsd-geom` `f56d65a4` | Captured the real output of `geom disk list`, `geom part list`, `glabel status -s` and `mount -p` (the test fixtures come from here) |
| [41270616207](https://github.com/JamBalaya56562/motioneye/actions/runs/41270616207) | `repro/freebsd-init` `c6cf4ba9` | rc.d, round 1: failed with the pidfile and initgroups errors (see the issues below) |
| [41275088899](https://github.com/JamBalaya56562/motioneye/actions/runs/41275088899) | `repro/freebsd-init` `56c78163` | rc.d lifecycle: start, recovery after `kill -9`, restart, stop, init run again |
| [41280512034](https://github.com/JamBalaya56562/motioneye/actions/runs/41280512034) | `repro/freebsd-init` `d8f9856b` | Final: the PATH fix, the geom listing, choosing a label-mounted partition in the UI |

- The `repro/*` branches are fork-only probes: `.github/workflows/freebsd-probe.yml` and `.github/freebsd/probe.py`. Never put them in the upstream PR
- Both 14.3 and 15.1 run in each job. To check again, push to `repro/freebsd-init` (on top of `enh/freebsd`) and the workflow starts
- The final run was on `d8f9856b`, before the `(null)` fix. That fix is in a pure function, so it was checked by unit test only (a test that fails without the fix, then passes with it)

## State of dev on FreeBSD (before this PR)

| Item | Result | Evidence |
|---|---|---|
| Server start, network camera, current picture | Works | 検証済み (14.3 / 15.1) |
| `relayevent.sh` (motion events) | Works: no more `sha1sum`, curl -f exit 0 | 検証済み. One of #1616's fixes was already done on dev |
| `update.get_os_version()` | Falls back to `uname` without `lsb_release` | 検証済み. Also already done |
| Config backup (#1060) | Works | 検証済み → **#1060 is a close candidate** (needs the user's OK) |
| Choosing a storage device | **Impossible**: `/proc/mounts` missing (`FileNotFoundError`), `/dev/disk/by-id` missing, and `fdisk -l` gives `fdisk: illegal option -- l` | 検証済み |
| `motioneye_init` | Runs `linux_init` → "neither APT nor YUM" warning; dies at `chown motion:motion` (no such group); installs no service | 検証済み |
| `smb_shares true` | Exits at startup with "please install cifs-utils" (`server.py:317`). This happens **before** reading `/proc/mounts` | 検証済み. Out of scope for this PR |

## Likely review questions and answers

Reply drafts are in English (5 lines or fewer). **A reply that disputes the review needs the user's OK before posting.**

### Q1. MichaIng asked in #2610 (2022) to fold the BSD setup into `linux_init` and cut duplicate code. Why a separate `freebsd_init`?

- Facts (コード根拠): `linux_init` is bash (`(( UID ))`, `[[ ]]`, `${DISTRO^}`, `grep -P`), and FreeBSD has no bash by default (paulprocacci in #2610). The shared parts are the root check, argument parsing, the `--meyectl` check and the config chown/chmod (about 20 lines). Everything else differs: apt/yum vs pkg, `motion` user vs `pw useradd motioneye`, `/etc` vs `/usr/local/etc`, systemd vs rc.d, motion.service handling
- Merging needs a POSIX sh rewrite of `linux_init` → that changes the Linux installer and is a big regression risk. In this PR I left the Linux side untouched
- Reply draft (**disputing, so get the OK first**):
  > I kept it separate so the Linux installer stays untouched: `linux_init` is bash, and apart from the argument checks and the config ownership every step differs (pkg, `pw`, `/usr/local/etc`, rc.d). Happy to merge both into one POSIX `sh` script in a follow-up if you prefer.
- If they say "merge it": rename to `motioneye/extra/init` (sh), branch with `case "$(uname -s)"`. Retest Linux in containers (Debian/Fedora/Arch) and FreeBSD on the VM

### Q2. Why switch to `mount -p` on `FileNotFoundError` instead of a `sys.platform` check?

- To fall back on any OS without `/proc/mounts`, not only FreeBSD (`mount -p` exists on the BSDs; 推測 for OpenBSD and NetBSD, 検証済み on FreeBSD only). Linux always has `/proc/mounts`, so its behavior does not change (コード根拠: the `open` succeeds and nothing else runs)
- `mount -p` prints the same 6 columns as `/proc/mounts` (fs, mount point, type, options, dump, pass) → `_list_mounts` parsing is unchanged (検証済み: sample from 15.1 in the test)
- FreeBSD separates columns with tabs, sometimes several; `split()` handles that (検証済み: the test fixture keeps the real tabs)

### Q3. Is `mount -p` alone enough?

- **No** (検証済み). `list_mounted_disks()` only marks the partitions returned by `_list_disks()` as mounted, so without a disk list no device is offered. That is why geom was added (the user chose 「geom も含める」)

### Q4. Why `geom` and not `fdisk`, `gpart show` or `camcontrol`?

- `fdisk` has no `-l` and FreeBSD 16 drops it (検証済み: the 15.1 output says `WARNING: fdisk is deprecated and is not available in FreeBSD 16 or later.`; 14.3 says "15 or later")
- `geom disk list` / `geom part list` cover every disk class (ada, da, nvd, vtbd, mmcsd) and their partitions in one call, in a `key: value` format that is easy to parse (検証済み on the VM output; the format is in geom(8) = ドキュメント根拠)
- `gpart show` prints a table that is harder to parse and shows sizes in sectors. `camcontrol` covers CAM devices only (推測; not compared)

### Q5. A memory disk (md) is not in `geom disk list`. Why can it be chosen?

- Verified: `geom disk list` only shows DISK-class devices; md devices are missing there but appear in `geom part list` (検証済み, run 41275336079)
- So a geom in the part list but not in the disk list is added as its own disk. That lets the VM test use md, and covers other providers that are not DISK class
- A real USB stick (da0) shows up in `geom disk list` (ドキュメント根拠 / 推測; we have no real hardware, and the VM had only vtbd0 and cd0)

### Q6. Why skip media of size 0?

- An empty optical drive (`cd0`) shows up with `Mediasize: 0 (0B)` (検証済み in VM output). It has no file system, so it cannot be a storage device

### Q7. What is `glabel` for? (`/dev/msdosfs/CAMS`, `/dev/gpt/...`)

- FreeBSD mounts by label: `/etc/fstab` and automount use `/dev/gpt/<label>`, `/dev/msdosfs/<LABEL>`, `/dev/ufs/<label>` (on 15.1, `/boot/efi` is mounted as `/dev/gpt/efiboot0`; 検証済み)
- `mount -p` shows the label path, while geom shows the partition (`md0p1`), so without matching them nothing is marked mounted. `glabel status -s` gives label → partition (検証済み: `msdosfs/CAMS N/A md0p1`)
- The storage device stays the partition (`local-disk-dev-md0p1`), so it does not change with how the partition is mounted. Saving and reading back keeps `storage_device local-disk-dev-md0p1` and `target_dir /media/cams/cams` (検証済み, run 41280512034)
- Labels are looked up only on FreeBSD (`sys.platform.startswith('freebsd')`); Linux runs no extra command (コード根拠)

### Q8. Is a ZFS dataset offered as a storage device?

- **No** (検証済み: with ZFS root on 15.1, only `/dev/vtbd0p2 at /boot/efi` is offered). `zroot/ROOT/default` is not a `/dev` partition, so it does not match. On Linux, btrfs subvolumes and NFS are not offered either; you use "Custom Path" (コード根拠: only partitions are listed). Not needed for this PR. ZFS support would be a follow-up
- On the 14.3 image the root is UFS, so `/dev/vtbd0p4 at /` is offered (検証済み). Linux offers the root partition the same way (コード根拠)

### Q9. Why did the vendor show `(null)`?

- FreeBSD 14.3 prints `descr: (null)` for virtio disks; 15.1 prints an empty field (検証済み, run 41280512034: `disk /dev/vtbd0 '(null)'`). `(null)` is treated as empty; the test fixture includes the 14.3 value. Without the fix the test fails with `'(null)' != ''`

### Q10. Why run rc.d through `daemon(8)`? Why not use meyectl's own background mode (`startserver -b`)?

- `startserver -b` exists (double fork, pid file in `run_path`, stopped with `stopserver`; コード根拠 `server.py` around L511–535). But in `-b` mode stdout and stderr go to /dev/null and output survives only in the log file, and nothing restarts the server when it dies. The Linux systemd unit also runs it in the foreground (no `-b`) with `Restart=on-abort` (コード根拠 `motioneye.systemd`). Same design here
- `daemon -f -r -S -T motioneye -P pidfile`:
  - `-r`: restarts it when it dies (like systemd's `Restart=on-abort`; 検証済み: started again after `kill -9`)
  - `-S -T`: output goes to syslog under the `motioneye` tag (検証済み: `/var/log/messages` gets `motioneye[pid]: INFO: hello! this is motionEye server ...`)
  - `-P`: the pid of daemon itself, so `service motioneye stop` stops the supervisor and the child together (検証済み)
- Same approach as many ports rc scripts (e.g. Python apps; 推測 — no specific port cited)

### Q11. Why not `daemon -u motioneye`? And why does the pidfile live in `/var/run/motioneye/`?

- With `motioneye_user=motioneye`, rc.subr already runs `command` through `su -m motioneye`. Adding `daemon -u` on top made a non-root process call `initgroups()`, which looped every second with `initgroups(motioneye,1001): Operation not permitted` (検証済み, run 41270616207). So `-u` was removed
- After that switch, daemon runs as motioneye and cannot create `/var/run/motioneye.pid`: `daemon: ppidfile /var/run/motioneye.pid: Permission denied` (検証済み). So `start_precmd` (as root) creates `/var/run/motioneye` owned by that user, and the pidfile goes there

### Q12. Why add `/usr/local/{s,}bin` to PATH in the rc script?

- rc.subr's PATH is `/sbin:/bin:/usr/sbin:/usr/bin` only. Without the change, the log said `motion not installed` and `v4l-utils not installed` (検証済み, run 41275088899). After the fix those warnings are gone (検証済み, run 41280512034). pkg puts motion, ffmpeg and v4l2-ctl in `/usr/local/bin`

### Q13. Why `REQUIRE: LOGIN`, and why install to `/usr/local/etc/rc.d`?

- Locally installed (non-base) services go in `/usr/local/etc/rc.d` and run after `LOGIN` by convention (ドキュメント根拠: FreeBSD Porter's Handbook / rc(8)). That also comes after the network and file systems

### Q14. Why a `motioneye` user instead of `motion` as on Linux?

- On Linux, the `motion` package creates `motion`. The FreeBSD `motion` pkg creates no user (検証済み: `chown motion:motion` failed with no such group). So we create our own user. The name follows #2610's script and FreeBSD habit (one user per service; 推測)
- If they want the `motion` name, only the defaults in `freebsd_init` and `motioneye.rc` change

### Q15. What is the `webcamd` group for? Was it tested with a USB camera?

- On FreeBSD, USB UVC cameras go through webcamd (`/dev/video*`), and the `webcamd` group gives access (ドキュメント根拠: webcamd(8)). Adding the user to the group only if it exists does nothing without webcamd
- **Not tested with a real USB camera (未検証)**: the VM has no camera. A network camera was tested (検証済み)

### Q16. Where do the conf, run, media and log paths come from? Is the config kept on a reinstall?

- `/usr/local/etc/motioneye` (conf, FreeBSD's place for non-base software), `/var/run/motioneye`, `/var/log/motioneye`, `/var/db/motioneye` (media; FreeBSD habit for persistent data, like `/var/lib` on Linux). Only these 3 lines are changed in `motioneye.conf.sample` with sed (MichaIng's "change only the lines that must differ")
- Running `motioneye_init --skip-rc` again keeps the existing config (検証済み, run 41275088899). Ownership `root:motioneye 0640` matches #3475 on Linux

### Q17. What about SMB shares (`smb_shares`)?

- Out of scope. FreeBSD mounts SMB with `mount_smbfs` (SMB1 only in base; SMB2/3 needs other tools, 推測), and `smbctl` assumes `mount.cifs`. `smbctl.list_mounts()` still reads `/proc/mounts`, and the server already exits earlier when `smb_shares true` (検証済み). We tried a fix but **dropped it** because it changed nothing that users can see
- If asked "why not use the `mount -p` fallback in smbctl too?": it changes nothing users see as long as the cifs-utils check exits first. Better to do it together with SMB support

### Q18. Test environment

- Upstream CI has no FreeBSD. Unit tests use the real output (captured from the VMs) as fixtures, so they run on Linux CI
- Full suite: 470 passed (検証済み: Docker `python:3.12-slim`, `git archive 299fa7aa`)

## Things that cost time (for next time)

- **vmactions/freebsd-vm takes about an hour** (installing from pip; PyPI ReadTimeout retries). The run script needs `set +e`, or the first failure (e.g. curl exit 7) aborts the rest
- **rc.d + `daemon`**: `motioneye_user` (rc.subr's su) and `daemon -u` together → initgroups EPERM loop. The pidfile must go in a directory the user owns. rc.subr's PATH has no `/usr/local`. Each needed a VM run to find (3 rounds)
- **`mount -p` alone shows nothing**: I first assumed "the disks can be chosen once mounts are readable" and told the user so; that was wrong. `list_mounted_disks` depends on `_list_disks` (fdisk) → geom added
- **smbctl fix pulled back**: `smb_shares` exits earlier on the cifs-utils check, so the `/proc/mounts` fix in smbctl had no visible effect. I had first claimed it was a fix
- **Line endings**: on Windows, Python `write_text` gives CRLF. Shell scripts are fixed to LF in `.gitattributes` (`freebsd_init`, `motioneye.rc`). Executable bit: `jj file chmod x`
- **Local tests**: wslc failed with E_FAIL even after 3 `wsl --shutdown`s → switched to Docker Desktop. A `cp -r` of the repo over a bind mount did not finish in 9 minutes (it includes `.jj` and more); `git archive <rev> | docker run -i ... tar x` finished in about 1.5 minutes. On Windows itself `fcntl` is missing, so only `tests/test_diskctl.py` and `test_motioneye_init.py` run (via `uv run --with ...`)
- **Cancelling a run**: `gh run cancel` hung past 2 minutes but did go through in the background

## Leftovers

- Submit the PR after #3506 or #3507 merges, then set assignee, v0.45.0 and labels (`enhancement`? check the labels upstream uses)
- #1060 (backup on FreeBSD) is a close candidate: works on dev (検証済み). Needs the user's OK. Close it after this PR is submitted, linking it
- Follow-ups: SMB on FreeBSD (`mount_smbfs`), ZFS datasets as storage, merging `linux_init` and `freebsd_init` (if the reviewers ask)
