# PR drafts

## `enh/conf-root-owned` — install motioneye.conf as root:motion 0640 (submitted as #3475, merged 2026-10-26)

- Branch: `JamBalaya56562:enh/conf-root-owned` (`faf38179`), base `dev` (`5acdd519`)
- Follow-up of #3474, suggested by MichaIng: https://github.com/motioneye-project/motioneye/pull/3474#issuecomment-6400316471 ("Side note")
- When: after some time has passed since #3474 was merged; one PR at a time

**Title:** `enh: install motioneye.conf as root:motion 0640`

**Body:**

```
Follow-up of #3474, as suggested there: motioneye.conf holds settings that the motionEye server is not meant to change itself, e.g. to lift its own restrictions via `motion_control_authentication` or `webcontrol_*`.

- `motioneye_init` (`linux_init`) now installs it as `root:motion` with mode 0640, so motionEye can read but not write it.
- The mode check in `meyectl` accepts access by root and motionEye's own user and group only, instead of always enforcing 0600:
  - access for others (or another group) is removed when motionEye owns the file,
  - otherwise (e.g. `root:motion 0644`) it asks the admin to apply the mode as root, since only the owner can change it,
  - a file owned by another user is reported.
- The sample notes the intended owner and mode.

Tested:
- Test suite: 348 passed, also when run as a non-root user.
- In a container with the `motion` user: `root:motion 0640` is read without warning and cannot be written by motion (`Permission denied`); `root:motion 0644` logs "please apply 0640 as root"; `motion:motion 0644` is changed to 0640.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

Before submitting: rebase onto the latest `dev`, re-run the tests, and re-check that no other open PR of ours exists.

## `enh/no-pid-file` — track motion by its process instead of a pid file (submitted as #3478, 2026-10-27, merged 2026-10-28)

- Branch: `JamBalaya56562:enh/no-pid-file` (`26010af1`), base `dev` (`5acdd519`)
- Related to #2540 (not closing it: the Docker entrypoint still needs root for `su motion`, see #3181 / #2407)
- When: after #3475 is merged; one PR at a time

**Title:** `enh: track motion by its process instead of a pid file`

**Body:**

```
Related to #2540: motionEye no longer needs a writable pid directory unless it runs in the background (`-b`).

- motionEye starts motion as its own child, so `motionctl` now keeps the `Popen` handle instead of writing `motion.pid` and reading it back. `running()` polls the process, `stop()` terminates it (TERM, then KILL, as before), and returns as soon as motion exited instead of always waiting 5 seconds.
- This also removes a hazard of the pid file: a stale `motion.pid` holding the PID of an unrelated process made motionEye treat that process as motion, skip starting motion, and terminate it on stop.
- `run_path` is only needed for `motioneye.pid` in background mode, so it is only checked there; the sample and settings comment say so.

This does not make `docker run --user` work yet: the entrypoint still creates `/run/motioneye` and switches to the motion user with `su`, which needs root (#3181).

Tested:
- Test suite: 353 passed, including new tests for the process handling and a stale pid file.
- With motion 4.5.1 as the motion user and a non-existent `run_path`: dev exits with "pid directory ... is not writable"; with this change motionEye starts, motion runs without any pid file, is restarted by the checker after `kill -9`, and is stopped with motionEye. With `-b`, the missing `run_path` is still reported.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

Before submitting: rebase onto the latest `dev`, re-run the tests, and re-check that no other open PR of ours exists.

## `enh/docker-puid` — run as PUID/PGID instead of the RUN_UID/RUN_GID build args (submitted as #3484, 2026-10-28)

- Branch: `JamBalaya56562:enh/docker-puid` (`23fd74f0`), stacked on `enh/no-pid-file` (#3478)
- Fixes #3181; related #2407, #2540
- When: after #3478 is merged; rebase onto dev first (one PR at a time)

**Title:** `feat(docker): run as PUID/PGID instead of the RUN_UID/RUN_GID build args`

**Body:**

```
Fixes #3181, as discussed there: the UID/GID motionEye runs as in the container can be chosen when the container starts, with the usual `PUID`/`PGID` environment variables, instead of only when building an image with `RUN_UID`/`RUN_GID`.

- `PUID`/`PGID` default to 0, so nothing changes without them: motionEye runs as root, as with the official images today.
- The entrypoint maps the `motion` user and group to them and hands the volumes over: `/etc/motioneye` on every start (it is small), `/var/lib/motioneye` only when its owner differs, as it may hold many recordings. Recordings made before, e.g. as root, are then owned by the new user, so the cleanup can remove them.
- `motioneye.conf` stays owned by root, as `motioneye_init` installs it (#3475): mode 0640 with group `PGID`, or 0600 when running as root, matching the mode check in `meyectl`.
- `RUN_UID`/`RUN_GID` are gone; a self-built image passes `-e PUID=... -e PGID=...` instead. `docker run --user` is still not supported, as the entrypoint needs root to do the above; the README says so.
- The entrypoint no longer creates `/run/motioneye`, which motionEye in the foreground does not need since #3478.

Tested with an image built from this branch, with named volumes:
- No `PUID`/`PGID`: motionEye runs as uid 0, `motioneye.conf` is `0:0` 0600, no mode warning.
- Same volumes with `PUID=1000 PGID=1000`: `motion` is 1000:1000 (still in `video`), motionEye runs as uid 1000, `motion.conf` is `1000:1000`, `motioneye.conf` is `0:1000` 0640, the media volume is handed over and a recording made as root can be deleted by the motion user.
- Restart with the same values: the media volume is not walked again.
- `PUID=abc`: the container exits with an error.
- shellcheck with the CI flags: clean.

**Release note:** the Docker image's `RUN_UID`/`RUN_GID` build arguments were replaced by the `PUID`/`PGID` environment variables, set when the container starts.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

Before submitting: rebase onto the latest `dev` (after #3478), rebuild the image and re-run the checks, and re-check that no other open PR of ours exists.

## `fix/layout-rows` — fit the layout rows into the window again (submitted as #3485, 2026-10-28)

- Branch: `JamBalaya56562:fix/layout-rows` (`60f79c52`), base `dev` (`a8390113`)
- Fixes #2583; supersedes #2590 (lowlyocean, idle since 2022)
- Screenshots: fork branch `pr-assets-layout-rows` (raw URLs in the body)
- Submitted 2026-10-28; screenshots in the live PR body are GitHub attachments

**Title:** `fix(ui): fit the layout rows into the window again`

**Body:**

````
Fixes #2583. Supersedes #2590, which has been idle since 2022; thanks to @lowlyocean for reporting and digging into it.

With "Fit frames vertically", the frames are meant to be sized so that "Layout rows" of them fit the window height. Since a25dec20 (2018, "improve updateLayout") the frame width is no longer divided by the rows, though the comment above still says so, and `layoutRows` has been an implicit global ever since. So a 2x2 layout always made each frame as tall as the whole window.

- `updateLayout()` divides the available height by the layout rows again (1 in single camera view and full screen, as for the columns), and takes the border and padding of a frame around its image into account, measured from a visible frame, since they add up per row.
- The ratio of a camera's picture was only recorded on its periodic refresh, so the first layout after the picture loaded could still use the placeholder ratio of 1. It is now recorded when the picture loads. With one row this hardly showed, as the page then usually takes the full width anyway.

Unlike #2590, this keeps the existing width-based layout: no row CSS classes, so any number of rows works, and with more cameras than rows × columns the extra ones simply continue below, as they do with columns today.

**Before / after**, four 640x480 network cameras, 2 columns × 2 rows, "Fit frames vertically" on:

| | Before | After |
|---|---|---|
| 1920x1080 | ![before 1920x1080](https://raw.githubusercontent.com/JamBalaya56562/motioneye/pr-assets-layout-rows/before-1920x1080.png) | ![after 1920x1080](https://raw.githubusercontent.com/JamBalaya56562/motioneye/pr-assets-layout-rows/after-1920x1080.png) |
| 1366x768 | ![before 1366x768](https://raw.githubusercontent.com/JamBalaya56562/motioneye/pr-assets-layout-rows/before-1366x768.png) | ![after 1366x768](https://raw.githubusercontent.com/JamBalaya56562/motioneye/pr-assets-layout-rows/after-1366x768.png) |

Measured with Playwright against current dev and this branch (frame size, bottom of the lowest frame):

| 1920x1080 | Before | After |
|---|---|---|
| 2 × 2 | 958x722, bottom 1493 | 679x512, bottom 1075 |
| 2 × 1 | 958x722 | 958x722 (unchanged) |
| 2 × 3 | 958x722 | 451x342 |
| 1 × 2 | 1025x772 | 679x512 |
| 2 × 2, settings panel open | 574x433 | 574x433 (the panel's width limit applies first) |
| single camera view | 1433x1078 | 1429x1075 |

At 1366x768 the 2 × 2 frames end at 763 (before: 1077), stable over repeated loads. No JavaScript errors, also when resizing the window.

The page can still scroll by its bottom padding (about 50 px) below the frames; that is unchanged and unrelated to the rows.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

Before submitting: rebase onto the latest `dev`, re-run the screenshots/measurements if `main.js` layout code changed, and re-check that no other open PR of ours exists.

## `fix/mask-conf-path` — write mask files to the configured conf_path (submitted as #3492, merged 2026-10-30)

- Branch: `JamBalaya56562:fix/mask-conf-path` (`169bd99d`), base `dev` (`5dc324ed`)
- Found while reproducing #2755; no issue reported yet
- When: when a PR slot is free (up to two open PRs)

**Title:** `fix(utils): write mask files to the configured conf_path`

**Body:**

```
Since #3324, `motioneye/utils` imports `CONF_PATH` from `settings` at import time. `meyectl` imports `utils` (through `config`) before `load_settings()` reads `motioneye.conf`, so the mask files are written to the built-in default, `sys.prefix` + `/etc/motioneye`, instead of the configured `conf_path`.

Where the two differ, saving a camera with an editable motion or privacy mask fails with a 500 error, e.g. with Python in `/usr/local`:

    FileNotFoundError: [Errno 2] No such file or directory: '/usr/local/etc/motioneye/mask_1.pgm'

That is the case in a venv (#3066) or with the python Docker images. With Debian's Python, `sys.prefix` is `/usr` and the default is `/etc/motioneye`, the same as `motioneye_init` configures, which is likely why it went unnoticed.

This reads `settings.CONF_PATH` when the file name is built, as before #3324. `utils` is the only module imported before `load_settings()` that binds a setting this way; the handlers that do are imported after it.

Tests:
- `tests/test_utils/test_mask.py` now patches `settings.CONF_PATH`, as `load_settings()` sets it, instead of `utils.CONF_PATH`; a new test checks that both mask files are written there. Against `dev`, all three tests fail with the error above.
- Full suite: 434 passed.
- In a python:3.12 container with `conf_path /etc/motioneye`: an editable motion mask edited and applied in the web UI is saved as `/etc/motioneye/mask_1.pgm` (before: the 500 error above).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

## `fix/mask-grid` — build the mask editor grid at the capture size (submitted as #3495, 2026-10-31, merged 2026-10-31)

- Branch: `JamBalaya56562:fix/mask-grid` (`09931ee4`), base `dev` (`f06fd23a`, rebased 2026-10-31 after #3493; 438 passed)
- Fixes #2755 (the part left after #3470: drift with the resolution dimmer)
- Screenshots: uploaded as GitHub attachments on 2026-10-30 (pasted into the #2755 comment box, not posted); already in the body below
- When: when a PR slot is free (up to two open PRs)

**Title:** `fix(ui): build the mask editor grid at the capture size`

**Body:**

````
Fixes #2755. #3470 fixed the drift at sizes with a remainder; this fixes the drift left with the resolution dimmer below 100 %.

The mask editor laid its grid out at the size of the preview picture, which the resolution dimmer scales down, while the server parses and builds the mask at the capture size. At 1024x768 with the dimmer at 80 %, the preview is 819x614: the editor makes 31 columns plus a remainder and 22 rows plus a remainder, while the server sends 32 × 24 lines. So the editor read the lines shifted, and each save sent 23 lines at 819x614, which the server drew at that size and stretched to 1024x768. The mask grew by a row on every save, even without editing it (the `editable mask needs resizing from 819x614 to 1024x768` in the report).

`getMaskSize()` now picks the size of the grid:
- the size at the start of the current mask lines, which the server sends at the capture size, so the lines and the grid always match;
- for a new mask, the configured resolution (or the custom one), with width and height swapped for a rotation of 90 or 270°, as the server does;
- the preview size only if the capture size is not known, as before.

The cells are placed in percent, so they still cover the scaled preview. The server is unchanged; it no longer needs to resize, as the lines now come at the capture size. A mask that already drifted stays as it is; its original shape is not stored anywhere.

**Before / after**, 1024x768 network camera, resolution dimmer at 80 %: a square mask drawn once, then the editor opened and saved three times without changes.

| Before | After |
|---|---|
| <img src="https://github.com/user-attachments/assets/f88a5e5e-91fe-4042-aea6-31369c8803a4" width="480"> | <img src="https://github.com/user-attachments/assets/8afc4228-e7f6-4479-8ff8-6391b35e907a" width="480"> |

Measured with Playwright against current dev and this branch: bounding box of the masked area in `mask_1.pgm` after each save (drawn: x 25–50 %, y ⅓–⅔).

| Case | Before | After |
|---|---|---|
| 1024x768, dimmer 80 % | bottom 541 → 575 → 609 → 642 | (256, 256, 512, 512) every time |
| 1640x1232, dimmer 80 % | stable, but off by up to 11 px | (416, 424, 832, 848) every time |
| 1024x768 rotated 90°, dimmer 80 % | stable, but off by about 20 px | stable, on the grid |
| 1024x768, dimmer 50 %, 5 %, 100 % | — | (256, 256, 512, 512) every time |
| privacy mask, dimmer 80 % | grows by a row per save | stable |

No JavaScript errors in any case.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `enh/layout-columns-per-browser` — keep the layout columns per browser (takes over #1570) (submitted as #3502, 2026-10-31, merged 2026-11-01)

- Branch: `JamBalaya56562:enh/layout-columns-per-browser` (`9fd0c0ce`), base `dev` (`dd1f79d4`, rebased 2026-10-31 after #3496; 459 passed; since `58c5f6cf` only translation JSON changed in the UI; earlier conflict in `main.js` with `getCameraImageRatio()` from #3491, both kept)

Title: `enh(ui): keep the layout columns per browser, from the window width by default`

> Takes over #1570 from @digiltd (credited as co-author), along the way discussed there: below 1200px the layout was always a single column with the slider hidden, because the columns were a per-user server preference shared by a desktop and a phone.
>
> - The layout columns are kept in the browser's local storage, so each device keeps its own. They are no longer sent to or read from `prefs.json`.
> - Until they are chosen in a browser, they follow the window width with about 500px per frame: 1 below 1000px, 2 below 1500px, 3 below 2000px, 4 from there.
> - The 1200px rule (single column, hidden slider) is gone; full screen and single view stay at one column.
>
> Columns chosen before are not carried over, as the stored value cannot be told from the old default of 3: each browser starts at the width-based value once.
>
> Not in here, for a later step: the other display preferences (rows, fit vertically, dimmers) in local storage too, a column limit by the number of cameras, an explicit "auto" in the slider.
>
> Checked with Playwright on 4 cameras (a `prefs.json` holding `layout_columns: 2` from before):
> - auto: 2200px → 4, 1920px → 3, 1400px → 2, 900px and 400px → 1 column, slider visible and following
> - 2 chosen at 400px: stored, kept after resizing to 1920px and after a reload; a fresh browser context still gets 3
> - saving another preference drops `layout_columns` from `prefs.json`
> - local storage blocked: auto columns, the slider still works for the page, no errors
>
> Supersedes #1570

## `enh/venv` — install into a venv (#3066) (submitted as #3496, 2026-10-31, merged 2026-10-31)

- Branch: `JamBalaya56562:enh/venv` (`e78a2908`, was `533e7c8b`), base `dev` (`58c5f6cf`, rebased 2026-10-31 after #3497 and #3468; 459 passed). Body: test_install noted as passed before the restart change (fork CI did not run on `a9d501c9`/`3e9eaad8`); pytest 440
- Review 2026-10-30 (MichaIng, COMMENTED): 3 inline suggestions (python3-venv into step 1 APT line, drop the step 2 APT line, drop the restart comment in linux_init) applied in `e78a2908` (first pushed as `4d9990cd` on the old base, replies edited), each replied "Done". Asked whether `VIRTUAL_ENV` could be used implicitly: replied it is unset when called via sudo or without activate (checked on Trixie), and motioneye_init already passes its own meyectl (issuecomment-6535141969)
- Fixes #3066; follows MichaIng's plan there (2024-10-19, 2026-02-22: `--meyectl`-like option for `linux_init`, passed by `motioneye_init`)
- Verified: 5 scenarios in a systemd Debian 13 container (2026-10-28), fork CI green on `f39efa29` (test_install 6/6, pre-commit); 439 passed on `699081c1`
- Pi (2026-10-30, Pi 5, trixie, Python 3.13.5, motion 4.7.1): switched the system-wide 0.44.0 install to a venv as in the README. `pip uninstall` worked (the Pi has `break-system-packages` in pip.conf), `ExecStart=/opt/motioneye/bin/meyectl`, `motioneye.conf` kept as `root:motion 0640`. **Found**: `motioneye_init` ends with `systemctl enable --now`, which does not restart a running service, so the old 0.44.0 process (from the removed `/usr/local/bin/meyectl`) kept running until `systemctl restart motioneye`; then 0.45.0a1 from the venv ran. Fixed in `a9d501c9` (user's choice, 2026-10-30): `linux_init` ends with `systemctl enable` + `systemctl restart`. Re-checked on the Pi: the running 0.44.0 (pid 7177) was replaced by 0.45.0a1 from the venv (pid 7630) without a manual restart; a stopped service is started and enabled. shellcheck as in CI clean, 439 passed; fork CI started on `a9d501c9`, not checked yet
- Pi: `motioneye_init` rewrites the unit, so a hand-edited `ExecStart=/usr/bin/libcamerify …` is lost (as on `dev`); a drop-in `/etc/systemd/system/motioneye.service.d/libcamerify.conf` (`ExecStart=` + `ExecStart=/usr/bin/libcamerify /opt/motioneye/bin/meyectl …`) survives a second `motioneye_init`, and the imx708 stream gave frames. Not part of this PR
- Labels to set: `documentation`, `Python`, `CI/CD`

**Title:** `feat(install): install into a venv, with the meyectl path passed by motioneye_init`

**Body:**

````
Fixes #3066

Recent Debian and Ubuntu versions do not allow `pip` to install outside of a venv, so the README worked around it with `break-system-packages` and `get-pip.py`. Simply installing into a venv was not enough: `linux_init` looks for `meyectl` in `/usr/local/bin` and `PATH`, where a venv's `bin` is not, so the systemd service failed to start (`ERROR: meyectl executable has not been found`, `status=203/EXEC`).

As suggested in https://github.com/motioneye-project/motioneye/issues/3066#issuecomment-3940839716:
- `linux_init` gets a `--meyectl PATH` option, used for `ExecStart` in place of the detection. A missing path, a directory or a missing argument aborts before anything is installed.
- `linux_init` restarts the service instead of `enable --now`, which left a running service on its old `ExecStart`, e.g. on the removed `/usr/local/bin/meyectl` after switching to a venv.
- `motioneye_init` passes the `meyectl` of its own Python environment (`sysconfig.get_path('scripts')`) if it is there, so it works from a venv without activating it. It is passed first, so `--meyectl` given on the command line takes precedence. Installed system-wide, this is `/usr/local/bin/meyectl`, as before.
- The README creates a venv in `/opt/motioneye` and installs, upgrades and sets up motionEye with its `pip` and `motioneye_init`. The `get-pip.py` and `break-system-packages` steps are gone. It also explains how to switch an install outside of a venv.
- `test_install` installs the same way, on all six runners.

Not changed: the Docker image (pip in the container) and the SysV init script.

## Testing

In a Debian 13 (Python 3.13) container with systemd:

| Case | Result |
|---|---|
| venv, `/opt/motioneye/bin/motioneye_init`, not activated | `ExecStart=/opt/motioneye/bin/meyectl`, service active, listening on 8765 |
| `--meyectl /usr/local/sbin/my-meyectl` | the given path is used, service active |
| missing path, a directory, no argument after `--meyectl` | error message, nothing installed |
| installed system-wide, as before | `/usr/local/bin/meyectl`, service active |
| system-wide install switched to a venv as in the README | `ExecStart` updated to the venv, service active; `motioneye.conf` (`root:motion` 0640) and lines added to it kept |

On a Raspberry Pi 5 (Raspberry Pi OS trixie, Python 3.13, motion 4.7.1), switching a running system-wide 0.44.0 to a venv as in the README: before the restart in `linux_init`, the old server from the removed `/usr/local/bin/meyectl` kept running until the service was restarted by hand; now `motioneye_init` replaces it with the one from the venv. A stopped service is started and enabled, as before.

- `tests/test_motioneye_init.py` (new): `--meyectl` is passed when the environment has `meyectl`, and nothing otherwise.
- `test_install` on my fork: all six jobs passed.
- shellcheck as in CI: no warnings. `pytest`: 439 passed.

Side note, not changed here: `motioneye_init` exits with 0 even when `linux_init` fails, as on `dev`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `fix/smb-keep-file` — stop at the target dir when removing empty folders, without .keep (#1810) (submitted as #3507, 2026-11-01)

- Branch: `JamBalaya56562:fix/smb-keep-file` (`9212ad3a`), base `dev` (`58c5f6cf`, rebased 2026-10-31 after #3497 and #3468; 463 passed)
- Fixes #1810; answers MichaIng's question there (2024-07-31) on why `.keep` was needed
- Verified: repro as `nobody` in a container (dev: target dir and its parent removed without `.keep`; read-only `.keep` → `[Errno 13] Permission denied: '…/.keep'`, file kept; branch: both fine). New tests fail on dev, each run alone; 443 passed; ruff OK
- Real SMB (2026-10-30, Docker: Samba 4.17.12 server, Linux 7.0 linuxkit CIFS client, mounted as motionEye does, target dir = mount root): **#1810 did not reproduce on dev** over SMB 2.1, 3.0, 3.1.1 with default Samba (`hide dot files = yes`, `.keep` gets attributes HA), `map hidden`/no `store dos attributes`, `hide files = /.*/`, or read-only create mode — overwriting the hidden `.keep` worked. The branch works on all of them (subfolders removed, mount root kept, an existing `.keep` left alone)
- SMB 1.0 and 2.0 on the Pi (2026-10-30, kernel 6.18 with `CIFS_ALLOW_INSECURE_LEGACY`, Samba 4.22.11 on the Pi itself with `server min protocol = NT1`, mounted as motionEye does): with default Samba, `map hidden`, `hide files`, **no repro on dev over 1.0, 2.0, 2.1, 3.1.1**. With `create mask = 0444` (new files read-only) over **SMB 1.0, dev shows the report exactly**: the first removal works, every later one fails with `[Errno 13] Permission denied: '…/.keep'`; the branch removes everything and keeps the mount root. Over 2.0+ that share could not be tested (setting the times of a new read-only file fails in the test script itself)
- Labels to set: `bug`, `Python`

**Title:** `fix(media): stop at the target dir when removing empty folders, without .keep`

**Body:**

````
Fixes #1810

To answer the question in https://github.com/motioneye-project/motioneye/issues/1810#issuecomment-2260579449: removing a media file or group in the UI, and the media cleanup, remove the emptied folders with `os.removedirs()`. That goes on with every parent that becomes empty, so without the `.keep` file it removes the camera's target dir as well, and further up whatever is left empty. The `.keep` file, written into the target dir before each removal, stopped it there.

On some SMB shares, that file becomes hidden and cannot be written again, so every removal after the first one fails with `[Errno 13] Permission denied: '…/.keep'`, as in the report.

This removes the emptied folders with a small helper instead, which stops before the target dir, and never removes it nor anything outside of it. So the `.keep` file is no longer needed and is no longer written. An existing one is left alone.

## Testing

As a non-root user in a container, with the target dir in a parent folder:

| Case | `dev` | This branch |
|---|---|---|
| cleanup of an old file in a subfolder, without `.keep` | the target dir and its parent are removed | only the subfolder is removed |
| removal in the UI, with a `.keep` that cannot be written (`chmod 444`) | `[Errno 13] Permission denied: '…/Camera1/.keep'`, the file is kept | removed |

On `dev`, running the tests without a `.keep` even removed the then empty `/tmp` of the container.

- `tests/test_mediafiles.py`: the cleanup tests no longer create a `.keep`, and check that the target dir and its parent are kept. New tests for `del_media_content()` and `del_media_group()`: emptied folders are removed up to the target dir, also for files directly in it and for the ungrouped files; folders with other files are kept; no `.keep` is written. Each new test fails on `dev`, except the one for folders with other files.
- Full suite: 443 passed.

On a real SMB share (Samba 4.17 server, Linux CIFS client mounted as motionEye does it, the target dir being the mount point), over SMB 2.1, 3.0 and 3.1.1: this branch removes the emptied folders and keeps the mount point, and leaves an existing `.keep` alone. With these dialects I could not reproduce the error itself: overwriting the hidden `.keep` worked, also with `map hidden` or `hide files`.

Over SMB 1.0 (Samba 4.22, `server min protocol = NT1`, on a Raspberry Pi 5 whose kernel allows it), the same holds with these settings. With a share that creates files read-only (`create mask = 0444`), `dev` shows the report exactly: the first removal works, as the `.keep` file does not exist yet, and every later one fails with `[Errno 13] Permission denied: '…/.keep'`. This branch removes everything there and keeps the mount point.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `enh/remember-me` — bring back "remember me" (#3364) (submitted as #3515, 2026-11-02)

- Branch: `JamBalaya56562:enh/remember-me` (`e1b06094`), base `dev` (`58c5f6cf`, rebased 2026-10-31 after #3497 and #3468; 459 passed); test fix: the session expiry is checked between the `Date` header and the request end, as the old `delta=1` failed once under load
- Related to #3364 (not Fixes: the PWA `SameSite` part stays open); follows MichaIng's idea of 2026-09-02 (no cookie lifetime → a true session cookie)
- Default off (user's choice, 2026-10-30), as in 0.43
- Verified: Tornado 6.5.10 drops `expires` with `expires_days=None`; Playwright: dialog shows the switch off, posts `remember=0/1`, cookie session (`expires -1`) vs 1 day; persistent profile closed and reopened → login dialog without, still logged in with; no JS errors. New test fails on dev (form and JSON), 439 passed, ruff, node --check
- Screenshot: scratchpad `remshots/dialog.png` (label shows "Memoru min" until translated)
- Labels to set: `feature`, `JavaScript`, `Python`
- Side finding, separate: `get_signed_cookie('user')` uses Tornado's default `max_age_days=31`, so `normal_session_expiry_hours` above 744 ends after 31 days (verified 2026-10-30, see README follow-up ideas)

**Title:** `feat(login): bring back "remember me"`

**Body:**

````
Related to #3364

As suggested in https://github.com/motioneye-project/motioneye/issues/3364#issuecomment-5514972264: the login dialog has a "remember me" switch again, off by default as in 0.43.

- Off: the session cookie has no expiry date, so the browser drops it when it is closed. Since 0.44.0 it always had one, so a login was kept after closing the browser, also on shared devices.
- On: the cookie lasts as long as the session, as now (24 hours for the admin, `normal_session_expiry_hours` for the surveillance user).

The session itself expires on the server as before either way, and the session store is kept, so logging out and changing a password still end the session on the server. API clients which do not send `remember` keep getting the lasting cookie, so e.g. the Home Assistant integration is not affected.

Not changed: the `SameSite=Strict` problem with PWAs, sessions surviving a restart (the cookie secret and the sessions live in memory), and renewing sessions.

The label uses the source string "Memoru min", which is no longer in the translations, so it shows untranslated until it is translated on Weblate.

## Testing

- New tests: with `remember=0` (form) or `false` (JSON) the cookie has no expiry date, while the session still expires after 24 hours on the server; with `1`/`true` it lasts 24 hours. The first fails on `dev`. Without `remember`, the existing lifetime tests still pass.
- Playwright against this branch: the dialog shows the switch off and posts `remember=0`, which gives a session cookie; switched on, `remember=1` and a cookie for 1 day. With a persistent browser profile closed and opened again: without "remember me" the login dialog comes up, with it the cameras show. No JavaScript errors.
- `pytest`: 439 passed.

| Login dialog |
|---|
| SCREENSHOT |

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `fix/session-cookie-max-age` — accept session cookies as long as the longest session lasts (submitted as #3510, 2026-11-01)

- Branch: `JamBalaya56562:fix/session-cookie-max-age` (`1100ca3c`), base `dev` (`58c5f6cf`, rebased 2026-10-31 after #3497 and #3468; 459 passed)
- Found while preparing `enh/remember-me` (#3364); follow-up of #3410. No issue
- Verified: probe on dev (1000 h: 200 at +30 days, 403 at +31.5/+40 while the session is still valid); new tests fail on dev (403 at +40 days; logout at +40 days leaves the session), pass on the branch; 439 passed; ruff
- Conflicts with `enh/remember-me` in `tests/test_handlers/test_login.py` (both add tests at the same place): rebase whichever goes second
- Labels to set: `bug`, `Python`

**Title:** `fix(login): accept session cookies as long as the longest session lasts`

**Body:**

````
Follow-up of #3410: Tornado rejects signed cookies older than 31 days, unless `get_signed_cookie()` is given another `max_age_days`. So a surveillance user session set to last longer with `normal_session_expiry_hours` (above 744) still ended after 31 days, although the browser kept the cookie and the session was still valid on the server. Logging out then did not end the session on the server either, as the logout reads the same cookie.

Both now read the session cookie with the longest session lifetime as maximum age. The session store keeps checking the lifetime of each user type, so the admin session still ends after 24 hours.

This only shows when motionEye runs for more than 31 days without a restart, as the sessions are kept in memory, e.g. for a kiosk display.

## Testing

With `normal_session_expiry_hours` at 1000 (41.7 days) and the clocks moved forward:

| Days after login | `dev` | This branch |
|---|---|---|
| 30 | 200 | 200 |
| 40 | 403, session still valid on the server | 200 |
| 42 | 403 | 403 (session expired) |
| logout at 40 | session kept on the server | session removed |

The two new tests fail on `dev` and pass here. `pytest`: 439 passed.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `enh/detection-action` — switch motion detection on and off with an action (#800)

- **Superseded by `fix/wsswitch-manual-detection` (2026-10-31).** Branch: `JamBalaya56562:enh/detection-action` (`d8ddeb56`), base `dev` (`1f81bcae`, rebased 2026-10-31). **Overlaps #3468** (MichaIng: temporary detection toggle, not saved); **#3468 merged 2026-10-31: rebase conflicts in `action.py` (its `detectionstart`/`detectionpause` vs our `detection_start`/`detection_pause`), left on `1f81bcae`.** What is left of it (saving `@motion_detection`, admin only) belongs to the follow-ups MichaIng wants as separate PRs; rework on top of #3468, not a rebase. Review comment posted 2026-10-31 (issuecomment-6526802944): working schedule undoes the pause, normal user can pause, OSError not caught, cache kept over a motion crash
- Fixes #800 (MichaIng put it on v0.45.0 on 2026-10-26). Admin only, decided by the user on 2026-10-30
- #1047 (trigger a detection or a recording) is already covered on `dev` by the `eventstart`/`eventend` and `record_start`/`record_stop` actions: possible close with this PR
- Pi (2026-10-30, motion 4.7.1, imx708 via libcamerify): pause/start/pause, and a motion restart while paused, gave the same results as in Docker (motion 4.5.1); stream still gave frames
- When: when a PR slot is free (up to two open PRs)

**Title:** `feat(action): switch motion detection on and off`

**Body:**

````
Fixes #800.

So far, the way to switch motion detection from a script was motion's own webcontrol (`/<id>/detection/pause`), which motionEye does not know about: the working schedule turns detection back on within 10 seconds, a motion restart brings back the saved state (`pause` is written from the motion detection switch), and the switch in the camera settings shows the old state.

Two new actions do what the motion detection switch in the camera settings does, without restarting motion:

```
POST /action/<camera_id>/detection_pause
POST /action/<camera_id>/detection_start
```

They save the switch in the camera config and apply it to the running motion at once. While paused, the working schedule leaves the camera alone, as with the switch turned off; `detection_start` hands it back to the schedule. As they change the camera config, they need the admin user (or a hub, for a remote camera, where the action is passed on to the remote). Cameras that motion does not handle (simple MJPEG) answer 400, as for other unknown actions.

## Testing

In a container with motion 4.5.1 and a network camera:

| Step | motion `detection/status` | camera-1.conf |
|---|---|---|
| `detection_pause` | PAUSE | `@motion_detection off`, `pause on` |
| `detection_start` | ACTIVE | `@motion_detection on`, `pause off` |
| paused, then motion killed and restarted by motionEye | PAUSE | unchanged |
| working schedule set, pause via motion's webcontrol, 25 s later | ACTIVE again | unchanged |
| working schedule set, `detection_pause`, 25 s later | PAUSE | `pause on` |

The same on a Raspberry Pi 5 with motion 4.7.1 and a Camera Module 3 (pause, start, and a motion restart while paused).

`/config/1/get` reports `motion_detection` false after `detection_pause` and true after `detection_start`, so the settings switch follows.

New tests in `tests/test_handlers/test_action_detection.py`: 5 of the 7 fail on `dev` (the other two, the 400 for an MJPEG camera and passing the action on to a remote, hold on `dev` too). `pytest`: 444 passed.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `fix/movie-cache-dir` — create the movie cache dir when caching, not on import (submitted as #3509, 2026-11-01)

- Branch: `JamBalaya56562:fix/movie-cache-dir` (`59e5fc3b`), base `dev` (`58c5f6cf`, rebased 2026-10-31 after #3497 and #3468; 458 passed). Pushed 2026-10-31, **not submitted** (user's call)
- Found while reviewing #3497 (Marijn0: separate `TMPDIR` per server in `hub_remote_compat.py`, as the 0.44.0 hub cannot be changed). This is the source side and stands on its own
- Why it matters outside CI (verified): Debian 13 has `q /tmp 1777 root root 10d`; with the age set to 2 s, `systemd-tmpfiles --clean` removed `/tmp/MotionEye` itself along with its old file. The unit has no `PrivateTmp`. On `dev`, a remote movie then fails with 500 (`FileNotFoundError` on `….part`) and `on_finish` logs `could not delete temp file`, until a restart
- Change: `os.makedirs(..., exist_ok=True)` in `_write_cache_file()`; no mkdir on import (so no race); `on_finish` returns while the dir does not exist
- Tests: new `test_the_cache_dir_is_created_again_when_removed` (fails on `dev` with the 500 above, passes here); 439 passed; importing the module leaves `/tmp/MotionEye` absent. Not run end to end: `hub_remote_compat.py` lists movies but does not play one

## `fix/wsswitch-manual-detection` — keep a manual detection change until the schedule changes (rework of `enh/detection-action`) (submitted as #3506, 2026-11-01, Closes #800)

- Branch: `JamBalaya56562:fix/wsswitch-manual-detection` (`9021b7b9`), base `dev` (`58c5f6cf`, after #3468). Pushed 2026-10-31, **not submitted**
- Replaces `enh/detection-action`, whose actions #3468 now provides. Follows MichaIng's wsswitch design in #3468 (issuecomment-6527827318): wsswitch caches the state it set per camera, checks and enforces again only when the intended state changes (schedule transition), after an error or a failed switch, or after `motionctl.start()`, which calls `wsswitch.clear_cache()` (imported inside `start()`, no circular import)
- Not included, as MichaIng wants them separately or not now: admin-only actions (he keeps them open to normal users), starting the loop only with a working schedule / `PeriodicCallback`
- Tests: new `tests/test_wsswitch.py` (5) + `test_the_working_schedule_checks_the_state_again` in `test_motionctl.py`; full suite 463 passed; ruff clean
- E2E (me-e2e, motion 4.5.1): schedule "during" all day, `detectionpause` → after 25 s still PAUSE (dev `58c5f6cf`: ACTIVE again). Schedule "outside" all day, `detectionstart` → stays ACTIVE; after `pkill motion` the checker restarts it and wsswitch pauses it again (cache cleared)

## `fix/action-buttons-rows` — arrange the action buttons when the camera overlay is shown (submitted as #3504, 2026-10-31, merged 2026-11-01)

- Branch: `JamBalaya56562:fix/action-buttons-rows` (`9eab8065`), base `dev` (`58c5f6cf`). Pushed 2026-10-31, **not submitted**: candidate once a PR slot is free (user)
- Reported in #3468 by Marijn0 (review 2026-10-30 19:42) and MichaIng (issuecomment-6534459865): with 2+ action buttons they stack until the layout is updated, the lower one outside the frame
- Cause (verified, Playwright on me-e2e): `updateActionButtons()` in `main.js` runs from `updateLayout()` while `div.camera-overlay` is `display: none`, so `camera-overlay-bottom` width is 0 → `cameraWidth <= actionsWidth` → `flex: 1 0 100%` for 2 buttons, one per row. `showCameraOverlay()` did not recompute
- Fix: skip when the width is 0, and call `updateActionButtons()` for all frames in `showCameraOverlay()` right after `display` is reset
- Checked at 1366x768, 2x2 layout: dev = 2 buttons stacked (bar 80 px high), fix = one row (40 px); a camera with 13 buttons still gets two rows (7 + 6) on both, also at 1920x1080. Merges cleanly with `enh/layout-columns-per-browser` and `fix/mask-grid`. Screenshots: scratchpad `btn/dev-load.png`, `btn/fix-load.png`

## `enh/smtp-implicit-tls` — choose none / STARTTLS / TLS for SMTP (takes over #2896)

- Branch: `JamBalaya56562:enh/smtp-implicit-tls` (`d89a0af0`), base `dev` (`58c5f6cf`). Pushed 2026-10-31, **not submitted**
- **Order (user, 2026-10-31):** after the #1570 takeover (`enh/layout-columns-per-browser`) and the other small branches. Meant as a prototype for MichaIng to try and take into #2896 or use as a base, not mainly to get merged
- #2896 (MichaIng, 2023-12) swaps STARTTLS for `SMTP_SSL`: breaking for 587 users (zagrim: Gmail 587 → `WRONG_VERSION_NUMBER`). Agreed there (MichaIng + zagrim, 2023-12-26): a plain/TLS/STARTTLS drop-down, old boolean → STARTTLS, port hints in the tooltip. Not done since; #2896 now conflicts with #3479
- Design: UI select `#smtpTlsSelect` (none/STARTTLS/TLS). Stored as the existing `@email_notifications_smtp_tls` + new optional `@email_notifications_smtp_implicit_tls` (TLS = both true). So old camera files, 0.44 hubs (key kept when absent, listed in `_NOT_FORWARDED`) and 0.44 remotes (ignore the new key → STARTTLS) all keep the old behaviour; no migration step. Old command lines migrate with implicit = False. Port tooltip rewritten (the old one said "465 for non-TLS")
- Checks (verified): pytest 464 passed (+7); ruff clean. Real SMTP (aiosmtpd, self-signed cert trusted by the system, verify on): TLS on an implicit-TLS port → sent; STARTTLS on a STARTTLS port → sent; STARTTLS against the TLS port → timeout; TLS against the STARTTLS port → `WRONG_VERSION_NUMBER`; none where STARTTLS is required → 530. UI (Playwright): verify row hidden for none, shown for STARTTLS/TLS; save → `tls True` + `implicit_tls True` in camera-1.conf, reload shows TLS; older answers (implicit absent) show STARTTLS / none. Screenshots: scratchpad `smtp/ui-{none,starttls,tls}.png`
- Related open issues: #2306 (Gmail), #2692 (Outlook "SMTP AUTH extension not supported")

### PR body draft

````markdown
Takes over #2896 from @MichaIng (credited as co-author), along the way agreed there with @zagrim: instead of turning "Use TLS" from STARTTLS into TLS, which would break the setups that work on port 587 today, the switch becomes a choice:

- **none**: a plain connection, as with the switch off
- **STARTTLS**: as "Use TLS" did so far, usually port 587
- **TLS**: encrypted from the start, usually port 465, as Gmail documents it

Meant as something to try out: feel free to take it into #2896 or change it, the UI wording in particular.

**Compatibility:** the existing `email_notifications_smtp_tls` setting stays, and TLS adds `email_notifications_smtp_implicit_tls`. Existing camera files, a 0.44 hub saving the camera, and a 0.44 remote all keep STARTTLS, so nothing changes until TLS is chosen. The "Verify certificate" switch from #3479 applies to both.

The port tooltip now names the usual ports (the old one said 465 for non-TLS).

**Tested:**
- pytest; and sending to a local SMTP server with a self-signed certificate trusted by the system: TLS on an implicit-TLS port and STARTTLS on a STARTTLS port both deliver; the wrong combinations fail as before (`WRONG_VERSION_NUMBER`, timeout)
- in the UI: the choice is saved, shown again after a reload, and the certificate switch shows only with STARTTLS or TLS

Supersedes #2896

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `enh/freebsd` — support FreeBSD: list the disks with geom, add an rc.d script (takes over #1616, closes #2610) (submitted as #3508, 2026-11-01)

- Branch: `JamBalaya56562:enh/freebsd` (`0983600f`), base `dev` (`5b492e1c`). Submitted as #3508 (body: 476 passed after the rebase)
- Investigation, verification runs and **answers to expected review questions**: [freebsd-support.md](freebsd-support.md)
- After submitting: assignee, v0.45.0, labels

**Title:** `enh: support FreeBSD: list the disks with geom, add an rc.d script`

````
Takes over #1616 for current FreeBSD (14.3 and 15.1), and adds the rc.d script asked for in #2610.

Supersedes #1616
Closes #2610

## What was still broken

I ran motionEye from `dev` on FreeBSD 14.3 and 15.1 VMs (packages: motion 4.7.1, python 3.12, py312-pycurl, py312-pillow). The server, a network camera, motion events relayed via `relayevent.sh`, the current picture and the config backup (#1060) all work as they are. Since #1616, the relay no longer uses `sha1sum`, and `update.get_os_version()` falls back to `uname` without `lsb_release`. What remained:

- **No local storage device could be chosen**: there is no `/proc/mounts`, no `/dev/disk/by-id`, and `fdisk` has no `-l` (and is removed in FreeBSD 16), so `diskctl` listed no disks.
- **`motioneye_init` ran `linux_init`**: it warned "neither APT nor YUM", failed at `chown motion:motion` (no such group), and installed no service.

## Changes

- `diskctl`
  - reads the mounts with `mount -p` where `/proc/mounts` does not exist. It prints the same columns (target, mount point, type, options).
  - lists the disks and their partitions with `geom disk list` and `geom part list` on FreeBSD. Disks without media (an empty optical drive) are skipped; memory disks, which are no disk geoms, are listed by their partition table.
  - finds partitions mounted by a label, like `/dev/msdosfs/CAMS` or `/dev/gpt/cams`, with `glabel status`, so the storage device stays the partition however it is mounted.
- `motioneye_init` runs the new `extra/freebsd_init` on FreeBSD. Like `linux_init`, it installs the dependencies (`pkg install motion v4l-utils ffmpeg curl`), creates a `motioneye` user (added to `webcamd` if present, for USB cameras), creates the config and data directories at the FreeBSD locations (`/usr/local/etc/motioneye`, `/var/run/motioneye`, `/var/log/motioneye`, `/var/db/motioneye`), installs the sample config with those paths, and installs and starts the rc.d service. It takes `--meyectl` like `linux_init`, and `--skip-rc` in place of `--skip-systemd`.
- `extra/motioneye.rc`: the rc.d script. `daemon(8)` runs `meyectl startserver` as `motioneye_user`, restarts it when it dies (like `Restart=on-abort`), and sends its output to syslog. The meyectl path, user and config path can be set in `rc.conf`; `freebsd_init` sets `motioneye_meyectl` to the meyectl of its Python environment, e.g. a venv.

SMB shares (`mount_smbfs` in place of `mount.cifs`) are left for a later PR.

## Tests

- `tests/test_diskctl.py`: mounts are read with `mount -p` when `/proc/mounts` is missing; disks are listed with `geom` (samples from FreeBSD 15.1, and the `(null)` description FreeBSD 14.3 prints for a virtual disk); a partition mounted by its label is found as the partition.
- `tests/test_motioneye_init.py`: `freebsd_init` is run on FreeBSD.
- 470 passed.

On FreeBSD 14.3 and 15.1 VMs (vmactions/freebsd-vm), from a venv with `motioneye_init`:

- the packages, the user, the directories and `motioneye_enable=YES` are in place, and `service motioneye status` reports it running; GET `/` returns 200, and syslog has the motionEye log, without warnings about motion or v4l-utils.
- after `kill -9` of meyectl, `daemon(8)` starts it again; `service motioneye restart` and `stop` work; running `motioneye_init --skip-rc` again keeps the config.
- a GPT memory disk with a FAT partition labelled `CAMS`, mounted as `/dev/msdosfs/CAMS` on `/media/cams`, is offered as `/dev/md0p1 at /media/cams`. Choosing it with root directory `/cams` saves `storage_device local-disk-dev-md0p1` and writes `target_dir /media/cams/cams` to the camera config.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `chore/ruff-lint-format` — replace black, flake8, isort and pyupgrade with ruff (stage 1)

- Branch: `JamBalaya56562:chore/ruff-lint-format` (`72006c2d`), base `dev` (`dd1f79d4`). Not submitted; the user picks the time (2026-10-31)
- Only `pyproject.toml` and `.pre-commit-config.yaml`. pre-commit on dev and on the branch: all hooks pass (hooks on Python 3.12 in the container instead of 3.14). New rules fire on a probe file: I001, UP035/UP006, E501 (133 > 125), C901 (71 > 68)

**Title:** `ci: replace black, flake8, isort and pyupgrade with ruff`

````
ruff already checks and formats the code in pre-commit. This lets it cover what four other hooks did, so that one tool and one config section remain:

- flake8: its `select` (`E9`, `F63`, `F7`, `F82`) is in ruff's defaults; `C901` and `E501` are added with flake8's limits (complexity 68, lines 125, the latter only for the check, the formatter keeps its own width).
- isort: ruff's `I` rules.
- pyupgrade: ruff's `UP` rules with `target-version = "py39"`.
- black: `ruff format` does this already. The black hook ran with `--diff`, so it only printed and never failed; with black 26.10.1 it differs from `ruff format` in three files (`sendtelegram.py`, `uploadservices.py`, `tests/test_notifications.py`).

On dev, flake8, isort and pyupgrade report nothing, and so do the ruff rules that replace them. The flake8 plugins (bugbear, comprehensions, 2020) did not run, as `select` limited flake8 to the codes listed; enabling the matching ruff rules (7 findings of B007, B027, B042) and the flake8-return rules noted in the config (`RET`) is left for later, as they need code changes.

bandit is replaced in a follow-up, as it needs comment changes in the code.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `chore/ruff-bandit` — replace bandit with the S rules of ruff (stage 2, on top of stage 1)

- Branch: `JamBalaya56562:chore/ruff-bandit` (`8137cc67`), base `chore/ruff-lint-format`. Not submitted; after stage 1 is merged (rebase then)
- 15 files: 34 `# nosec` → `# noqa: S…` or dropped; `per-file-ignores` S310 for `uploadservices.py` and `webhook.py`; one `ruff format` reflow in `uploadservices.py` (a line got short enough). pre-commit all pass, 459 passed. Probe: S602, S310, S301, S110 fire on new code
- Not covered by ruff (checked): B402 `ftplib` import (S402 is preview-only), B602 on `utils.call_subprocess(shell=shell)` (the real `shell=True` caller in `v4l2ctl.py` is S604)

**Title:** `ci: replace bandit with the S rules of ruff`

````
Follow-up to #NNNN. ruff has the bandit checks as its `S` rules, so the bandit hook can go as well:

- The rules bandit skipped are ignored in ruff too: `S105`, `S324`, `S404`, `S603`.
- ruff does not read `# nosec`. The 34 of them become `# noqa: S…`, or are dropped where the rule is ignored anyway (`S105`, `S324`) or where ruff does not report it (the `ftplib` imports, `call_subprocess(shell=shell)`).
- ruff's `S310` also reports building a `Request` with a variable URL, which bandit did not. `uploadservices.py` and `webhook.py` only build requests and open them with `utils.urlopen()`, which allows only http and https, so `S310` is ignored in these two files.

Not covered by ruff: the `ftplib` import warning (`S402` is a preview rule) and `shell=` passed on as a variable in `utils.call_subprocess()`; the `shell=True` call in `v4l2ctl.py` is still reported (`S604`).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `fix/sftp-test-lowercase` — remove the SFTP test file with lower case commands (not submitted)

- Branch: `JamBalaya56562:fix/sftp-test-lowercase` (`b826859a`), base `dev` (`9bd19a00`). Labels: `bug`, `Python`
- Review Q&A: "Did it ever work?" → yes with libcurl 7 (bookworm 7.88.1: `RM`/`RMDIR` OK); libcurl 8.14.1 (trixie) and the pycurl 7.49.0 wheel (libcurl 8.23.0) refuse them. Which libcurl release changed it was not looked up (未検証)

Title: `fix(upload): remove the SFTP test file with lower case commands, as libcurl 8 needs`

````markdown
The SFTP "Test service" button uploads a file, then removes it and its folder with `RM` and `RMDIR` as `CURLOPT_POSTQUOTE` commands. libcurl 8 takes only the lower case commands its documentation lists, so the test always fails with `(21, 'Unknown SFTP command')`, and `motioneye_test/<time>` stays on the server. Uploads themselves are not affected.

The commands are now `rm` and `rmdir`.

Checked against a real OpenSSH server in a container, with password login:

| libcurl | `RM`/`RMDIR` (dev) | `rm`/`rmdir` (this PR) |
|---|---|---|
| 7.88.1 (Debian bookworm, python3-pycurl) | test passes, nothing left | test passes, nothing left |
| 8.14.1 (Debian trixie, python3-pycurl) | `Unknown SFTP command`, file left | test passes, nothing left |
| 8.23.0 (pycurl 7.49.0 wheel from PyPI) | `Unknown SFTP command`, file left | test passes, nothing left |

A wrong password still fails the test with `Authentication failure`.

**Tests:** `TestSFTPTestAccess` checks the upload URL and the two commands; it fails with the upper case ones. 504 passed on Python 3.9 and 3.12.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `enh/upload-optional-modules` — import boto3 and pycurl only for S3 and SFTP (not submitted)

- Branch: `JamBalaya56562:enh/upload-optional-modules` (`3ec263a8`), base `dev` (`9bd19a00`). Labels: `enhancement`, `Python`. Rebase after `fix/sftp-test-lowercase` (both touch `SFTP.test_access`)
- Step 2 of dropping pycurl (MichaIng on #3511: "making the modules needed for particular upload services optional, gracefully handling their absence"); #3516 body: "the upload services come next"
- Decisions (1 and 2 confirmed by the user on 2026-11-03):
  1. boto3 dropped from `dependencies` (fresh installs lack it; `pip install --upgrade` keeps an installed one). Alternative: keep it required, only import lazily
  2. No `[project.optional-dependencies]` extra (`motioneye[s3]`): the error message and README name the module directly
  3. Docker image installs boto3 (images have no easy way to add it)
- Review Q&A: CI (`test_python.yml`) still installs boto3 and boto3-stubs explicitly, for the S3 tests and mypy; the missing-module case is simulated with `sys.modules[...] = None`

Title: `enh(upload): import boto3 and pycurl only for S3 and SFTP uploads, boto3 no longer required`

````markdown
Next step of dropping pycurl, as discussed in #3511: the modules of single upload services are optional now.

- `boto3` and `pycurl` are imported when an S3 or SFTP upload or test runs, no longer when motionEye starts. Without the module, only that service fails, and its test (and the log for uploads) says what to install, e.g.
  `S3 uploads need the Python module boto3, install it with: /opt/motioneye/bin/python -m pip install boto3`
- `boto3` is no longer installed with motionEye. The README tells S3 users to add it; the Docker image keeps installing it. An existing installation keeps it on upgrade, as pip does not remove it.
- `pycurl` stays required until Telegram (#3514) and the Tornado client (#3516) no longer use it.

boto3 is the largest dependency: botocore alone is 31 MB in the venv, and importing boto3 took 0.43 s and 27 MB of memory (Python 3.12, x86_64), which every motionEye paid without using S3.

**Checked** in a container with a venv installed from this branch:
- boto3 is not installed; after importing the upload services and the server, neither boto3 nor pycurl is loaded
- SFTP to a real OpenSSH server: upload works, a wrong password fails the test with `Authentication failure`
- S3 test without boto3: the message above; after `pip install boto3`, the test reaches the endpoint (`Could not connect to the endpoint URL`)

**Tests:** `TestOptionalModules`: the module import loads neither, the test says what to install, an upload fails and keeps the local file (also with "remove after upload" on), the services are still offered, and the SFTP options exist on a real `pycurl.Curl`. The S3 tests patch `boto3.client` instead of the module attribute. 508 passed on Python 3.9 and 3.12, mypy clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `chore/ruff-return` — add ruff's flake8-return rules → **submitted as [#3547](https://github.com/motioneye-project/motioneye/pull/3547)** (2026-11-12, `b8403379` on dev `e765d633`; +229/−261, +69/−101 with `?w=1`; 3.9: 563 passed; labels CI/CD, Python; milestone v0.45.0)

- Branch: `JamBalaya56562:chore/ruff-return` (`0285dc62`), base `dev` (`925dcc07`). Labels: `CI/CD`, `Python`
- Origin: before #3519 the flake8 config said "flake8-return rules to add after its next release ...
  R501..R508"; #3519 kept it as "RET501 to RET508 to add later". `extend-select` gets `"RET"` (the whole
  family is RET501 to RET508 in ruff)
- 46 findings: RET505 40, RET504 3, RET503 1, RET507 1, RET508 1. ruff's safe fixes for the 42
  (else/elif after return, raise, continue, break), 4 by hand: 3 assignments before return
  (`config.add_camera`, `get_movie_duration_seconds`, `build_mask_file_name`), `set_camera_config` in
  `handlers/config.py` returned `on_finish(...)` in one branch only (now call + `return`)
- 16 files, +235/-267. 3.9: ruff, format, mypy clean, 550 passed
- Conflicts with #3545 on the `extend-select` line; rebase after it merges, then submit (user)

## `fix/video-params-palette` — keep motion's own video_params entries (#2635) → **submitted as [#3551](https://github.com/motioneye-project/motioneye/pull/3551)** (2026-11-13, `59f1aa31` on dev `20bba78f`; 581 passed; labels bug, motion, Python; v0.45.0; #2635 relabelled −feature −legacy motionEye +bug)

- Branch: `JamBalaya56562:fix/video-params-palette` (`84f93957`), base `dev` (`e765d633`). Fixes #2635
  (milestone v0.45.0). Labels: `bug`, `Python`, `motion`
- Cause: `video_params` is rebuilt from the detected controls on each save (`config.py` v4l2 branch of
  `motion_camera_ui_to_dict`), and on read the whole line becomes `vid_control_params`, so a
  `palette=15` set by hand or through Extra Options is gone after the next save. #3458 fixed the
  `netcam_params` half of the issue; free-cup-holder-exe noted the palette part remained
- Fix, as #3458: on read (`_MOTION_44_TO_43`), motion's own entries (`palette`, `input`, `norm`,
  `frequency`; Motion docs: they replaced `v4l2_palette`, `input`, `norm`, `frequency` in 4.4) go to an
  extra `video_params` option, shown in Extra Options; on write (`_MOTION_43_TO_44`) it is put in front
  of the controls. Split by commas outside double quotes (Motion allows `"Gain, Automatic"=1`)
- Tests (`tests/test_config.py`): 5 mapping tests + 2 through the file (V4L2 camera with
  `palette=15,ID09963776=10`: shows in Extra Options; a save with brightness 20 writes
  `palette=15,ID09963776=20`). On dev: 4 of the 7 fail (save gave `video_params ID09963776=20`).
  3.9 in Docker: ruff, format, mypy clean, 570 passed
- Not checked on a real camera (Pi off). Expected review Q: a palette set in Extra Options while
  the camera also had one in the file: the extra option replaces it (it is the same entry read back)

## `refactor/handlers-return-none` — handlers return nothing, `-> None` (not submitted, after #3547)

- Branch: `JamBalaya56562:refactor/handlers-return-none` (`0dde9e57`+), **stacked on `chore/ruff-return`
  (#3547)**; rebase onto dev once #3547 merges. Idea: MichaIng on #3547 (pullrequestreview-5866966003)
- 120 `return <finishing call>` (finish, finish_json, finish_json_with_error, render, try_finish, ...)
  rewritten by an ast script to the call plus `return` where code follows; `-> None` on the handler
  methods that return nothing; ruff RET501 removed 21 `return None`. Not annotated: methods that return
  values, Tornado's `finish`/`render` overrides, and BaseHandler's fallback `get`/`post`/`head` (as
  `-> None` they clash with the async subclasses: mypy override errors, 7)
- Annotating made mypy check those bodies, which found 4 more (fixed): `Popen.stdout` Optional in
  `check_command` (now `communicate()[0]`, the process has ended), `resp` reused for two response types in
  `ConfigHandler.list` (loop var renamed), `_upload_service_test_info` undeclared (class attribute),
  and RET502 in the auth wrapper (`return None`, it returns `func(...)` elsewhere)
- 3.9 Docker: ruff, format, mypy clean, 563 passed
- What enforces it (verified with mypy and ty 0.0.101 on a probe): with `-> None`, returning a Future
  (Tornado's `finish`/`render`) is an error in both; NOT caught by either: `return self.finish_json()`
  (it is `-> None`, type-correct) and `return self.finish()` while BaseHandler.finish is unannotated.
  ruff ANN201/ANN202 could require the annotations in handlers only
  (`per-file-ignores "!motioneye/handlers/**"` works in ruff 0.17.4)
- 2026-11-12 (user: type finish): `BaseHandler.finish(chunk: str | bytes | dict | None = None) -> Future[None]`
  (Tornado's signature; `from __future__ import annotations` added to base.py); once finished it answers a
  done Future instead of None (no caller uses the value; test `test_finish_once_finished_answers_a_done_future`).
  Probe: `return self.finish({...})` in `-> None` `restore()` -> mypy `No return value expected`;
  `return self.finish_json(...)` still passes (type-correct, review only). 3.9: 564 passed; 3.14: handlers 157 passed

## fix/threshold-min (Fixes #1895), 2026-11-12 → **submitted as [#3548](https://github.com/motioneye-project/motioneye/pull/3548)** (2026-11-13)

Branch `fix/threshold-min` `bde12598` on dev `e765d633`; rebased to `70de6e90` on dev `413b7ce4` and submitted (3.9: ruff, format, mypy clean, 566 passed; labels bug, Python, motion; milestone v0.45.0).

- The Frame Change Threshold slider has `min="0"` (`main.html:871`); 0 % was written as `threshold 0`
  (`config.py`, three places in `motion_camera_ui_to_dict`).
- Motion 4.7.0 source (release-4.7.0 `src/motion.c:2046`): `if (cnt->threshold && !cnt->pause)` wraps
  the diff, so threshold 0 means no motion detection (matches lowlyocean's report in #1895). Motion
  4.7.0 in a trixie container accepts and prints `threshold 0` without a warning.
- New `_threshold_pixels(percent, width, height)` = `max(1, int(percent * w * h / 100))`; 3 tests in
  `TestThresholdPixels`.
- Python 3.9 in Docker: ruff, ruff format, mypy as in CI (`mypy .`, 111 files) clean; 558 passed.
- Not tried on a camera.

Pi 5 check, 2026-11-12 (Camera Module 3 through libcamerify, motion 4.7.1, 640x480 at 2 fps,
minimum_motion_frames 20, auto threshold tuning off). 0 % set through the UI API (`POST /config/0/set/`
after `/login/` as admin, same path as Apply; the UI itself refused Apply with the empty passwords):

| | camera-1.conf | events in 60 s, nothing moving | events in 60 s, hand waved ~20 s |
|---|---|---|---|
| dev `e765d633` | `threshold 0` | 0 | 0 |
| `fix/threshold-min` `bde12598` | `threshold 1` | 0 | 1 (`received relayed event start`) |

Counted from motionEye's debug log (log_level debug for the test). Pi restored from
`~/meye-backup-1895`; motionEye left on dev `e765d633` (was 0.45.0b1 from an older /tmp/me).
Seen on the way: a GET with `Content-Type: application/json` and no body gives 500 in
`BaseHandler.get_json()` (our test script sent it; browsers do not). Not in this PR.

## fix/json-body (no issue), 2026-11-12 → **submitted as [#3552](https://github.com/motioneye-project/motioneye/pull/3552)** (2026-11-13, `efe0d8b4` on dev `20bba78f`; 577 passed; labels bug, Python; v0.45.0)

Branch `fix/json-body` `bceff3ad` on dev `e765d633`, pushed to the fork, no PR yet. Found during the
#1895 Pi check (our script sent `Content-Type: application/json` on a GET).

- `BaseHandler.get_json()` (`handlers/base.py:120`) ran `json.loads()` on any body with that type:
  an empty body and broken JSON both gave 500. Now: no body, no JSON; broken JSON is
  `HTTPError(400, 'invalid json body')` (same text as `set_credentials()`, `handlers/config.py:137`).
  `_json` is only set after a successful parse.
- Tests in `tests/test_handlers/test_base.py`: `test_get_argument_invalid_json` now expects 400 (it
  expected `JSONDecodeError`), plus no-body unit test, GET `/login` with the header (403), POST
  `/login` with broken JSON (400 + `{"error": "invalid json body"}`). All 4 fail on dev.
- Python 3.9 in Docker: ruff, ruff format, `mypy .` (111 files) clean; 566 passed.
- Whether any real client (e.g. the Home Assistant integration) sends the header on a GET: not checked.

## fix/webhook-percent (#2818) — prepared 2026-11-12 → **submitted as [#3549](https://github.com/motioneye-project/motioneye/pull/3549)** (2026-11-13)

Rebased to `108d9035` on dev `413b7ce4` (3.9: ruff, format, mypy clean, 564 passed; labels bug, Python, motion; milestone v0.45.0).

Commit 092e4ea3 on dev e765d633. `config.py`: `_webhook_url_to_motion()` writes `%` followed by a digit and a hex digit as `%%` in the three webhook URLs (4 lines: event start, event end, movie end, picture save); `_webhook_url_from_motion()` turns it back when the settings are read. Motion's specifiers (`%t`, `%D`, `%{fps}` in HA's URLs) stay.

Evidence:
- Motion 4.7.0 in Docker (debian:trixie-slim, MJPEG test source, `emulate_motion on`), `on_event_start echo '...'`: `power1%20on` → `power1                1500n` (20 read as the width of `%o`, the threshold); `power1%%20on` → `power1%20on`; `cam%t` → `cam0`.
- New test `test_percent_encoding_in_a_webhook_url_reaches_the_service` fails on dev (URL passed with `%20`), passes on the fix.
- Python 3.9: ruff, ruff format, `mypy .` (111 files) clean; 564 passed.

Not covered: letter-first encodings like UTF-8 `%C3%A9` stay as Motion specifiers (`%C` is the event text), as before. A webhook URL with a width on a specifier like `%02d` is now sent literally.

Expected review Q&A:
- Why not escape every `%`? HA and others use Motion's specifiers in the URL on purpose.
- Old configs with `%20`: shown as `%20`, saved as `%%20` on the next save; a URL typed as `%%20` before stays `%%20` in the file and shows as `%20`.

#3548 / #3549 reviews (2026-11-12): both approved by Marijn0 and MichaIng, no changes asked. MichaIng on #3549: users may use specifier widths or escape `%` themselves (checked on the branch: `%%20` stays `%%20` in the file, the UI then shows `%20`; `%02d` is sent literally), and suggested documenting Motion's `%` handling. 2026-11-13: wiki page [Motion Conversion Specifiers](https://github.com/motioneye-project/motioneye/wiki/Motion-Conversion-Specifiers) added (wiki `5b4e81c6`, linked from Configuration and the sidebar; facts from Motion 4.7.0 `util.c:464`, `event.c:86`, `motion.c:2289-2297`, the Docker repro and en.po labels) and a short reply posted on #3549.

#3546 review thread on the motion version note (2026-11-13): MichaIng suggested "motion 4.7.0 or newer is recommended" (zombies no hard blocker, arm64 fix maybe backported). Checked: Debian bookworm motion 4.5.1-2 has only `change-paths_set-debian-paths.patch` (sources.debian.org), archive.raspberrypi.com bookworm arm64 has no motion package, so bookworm arm64 still fails (Motion-Project/motion#1644). Compromise with the user's OK: 78c3eab0 "motion 4.7.0 or newer is recommended: older versions leave zombie processes behind, and before 4.6.0 they fail on arm64" (comment only; no test reads the sample), reply posted (discussion_r4557355307).
Open: MichaIng's issue comment (2026-11-12 22:47): drop libcamerify, install only libcamera-v4l2 and put `LD_PRELOAD=<path of v4l2-compat.so>` on the motion and v4l2-ctl calls. Needs a plan with the user (changes the setting's name and text).

#3546 rework (2026-11-13, PR set to draft by the user): c92ee147 replaces libcamerify with `libcamera_v4l2` (path of v4l2-compat.so), added to LD_PRELOAD for motion (`motionctl.start` env) and the 3 v4l2-ctl calls (`utils.libcamera_v4l2_env()`, not twice, missing reported once); re-exec and MOTIONEYE_LIBCAMERIFY removed; `motioneye_init --libcamera/--no-libcamera` installs only libcamera-v4l2 and writes the `dpkg -L` path. libcamerify.in (Debian 0.4.0) only sets LD_PRELOAD; path `/usr/libexec/<triplet>/libcamera/v4l2-compat.so` in Debian trixie and RPi 0.8.0+rpt. Checked: 3.9 Docker ruff/format/mypy clean, 571 passed, shellcheck 0.10.0 with CI flags clean; trixie container: init writes the path, motion has LD_PRELOAD, meyectl not. PR title/body updated, reply posted (issuecomment-6839445125).
TODO when the Pi is on: Camera Module 3 with only libcamera-v4l2 (no libcamerify wrapper), add camera, picture, resolutions/name as in the old table, zombies; then mark ready.

2026-11-13, before merging #3548/#3549: #1895 −question +bug +motion, #2818 −troubleshooting +bug +motion, both milestone v0.45.0; linked to the PRs through "Fixes" (closingIssuesReferences 1895 / 2818), so the merges close them.

## Prepared 2026-11-13, not submitted (all on dev 3da795c7, Python 3.9 Docker: ruff, format, mypy clean)

- `fix/unsupported-locale` (Fixes #2952): `load_l10n()` catches `locale.Error` from `setlocale(LC_ALL, '')`, warns, keeps C. Docker: `LANG=de_DE.UTF-8 meyectl startserver` dies with `locale.Error` on dev, starts with the warning on the branch. Test in `tests/test_l10n.py`. 571 passed. No Pi needed.
- `fix/listen-ipv6` (Fixes #779): a text option without a value is empty, so `listen` alone listens on 0.0.0.0 and [::] (Tornado, empty address); sample and settings.py describe 0.0.0.0 / :: / bare `listen` / 127.0.0.1, ::1. Docker `ss -ltn`: dev `listen` → invalid line, `listen ''` → gaierror; `listen ::` → [::] + 127.0.0.1 (relay), IPv6 only (V6ONLY, both bind); branch `listen` → 0.0.0.0 + [::]. 3 tests in `tests/test_meyectl.py`. 573 passed. Optional on the Pi: reach the UI over IPv6 from the LAN.
- `fix/dropbox-refresh-log` (Fixes #3128): the retry after a refreshed token is outside the refresh's try, so its failure is not "refreshing credentials failed"; Dropbox's body reason (`error_summary`, else `error`) is logged; the not_found check reads that reason (it looked at "HTTP Error 409: Conflict" before). 6 new tests, 3 fail on dev with the issue's exact log sequence. 576 passed. To check with a temporary Dropbox account (user, at home): the real 409 body has `error_summary` (only seen in the SDK reading the JSON body for 403/404/409, not verified), and a missing folder now gives `folder ... not found`.

2026-11-13: #3549 merged (dev 20bba78f), fix/webhook-percent deleted locally and on the fork; #2818 closed with v0.45.0.

2026-11-14: `fix/unsupported-locale` → **submitted as [#3553](https://github.com/motioneye-project/motioneye/pull/3553)** (`cc647c32` on dev `d9ec417d`; 3.9: ruff, format, mypy clean, 597 passed, shellcheck clean; labels bug, Python; v0.45.0; Fixes #2952). `fix/listen-ipv6` → **submitted as [#3554](https://github.com/motioneye-project/motioneye/pull/3554)** (`94ff99de`; 599 passed; labels enhancement, Python; v0.45.0; Fixes #779; IPv6 from the LAN not tried on the Pi). Also 2026-11-14: #3552 and #3551 merged, branches deleted; #3546 round 2 in one-pass-2026-11.md.

2026-11-14 Pi check for #3554 (Pi 5 trixie, branch 94ff99de, bare `listen`): `ss -ltn` shows 0.0.0.0:8765 and [::]:8765; from the Windows PC on the same /64, curl to the Pi's global IPv6 and to 192.168.0.6 both HTTP 200, and the in-app browser opened the UI over IPv6 and logged in. Added to the PR description. Pi restored to #3546 (2c9f3374) with its conf.

Dropbox (#3128): the released 0.44.0 wheel still has `CLIENT_ID = 'dropbox_client_id_placeholder'` (and the secret), as on dev since aefb88ff "removed dropbox app keys from git"; no workflow fills them in. So "Obtain Key" cannot work on any current install (cf. closed #1958, #171). A real-account check of #3128 needs a Dropbox app of our own (app key/secret from the App Console) put in locally.

2026-11-14: #1958 reopened with the Dropbox key analysis (issuecomment-6866196557, re-posted with an @MichaIng mention so that he gets notified): placeholders in dev and the 0.44.0 wheel, Dropbox's authorize page answers `unknown_client_id` (checked in the browser), python2 `setup.py` filled them from `extra/dropbox.keys` at build time, no workflow does now, the UI has no app key field. Options for the maintainers: project app + secrets in pypi_release.yml, user-supplied app key/secret, or removing the Dropbox service (user's request to include it). Labels: −question (bug, docker kept). Not checked: whether the old motionEyeOS keys still work (fetching them was not allowed). #3128 real-account test waits for this, or for a test app of our own.

## Prepared 2026-11-14, not submitted (on dev d9ec417d; Python 3.9 Docker: ruff, format, mypy clean, shellcheck clean)

- `fix/picture-dialog-load` (Fixes #2214, `e7625cc9`): `updatePicture()` added a `load` handler per picture; now `img.off('load.pictureDialog').on('load.pictureDialog', …)`. Checked in the in-app browser (Docker, MJPEG test camera, 1 s interval pictures): load handlers on the dialog's picture after opening and 6 "previous" clicks — dev 2,3,4,5,6,7,8; branch 2,2,2,2,2,2,2. 596 passed.
- `fix/threshold-tuning-order` (Fixes #1349, `59d6c76e`): Auto Threshold Tuning row moved above the two rows that depend on it, as the noise rows already are. DOM order checked in the browser: autoThresholdTuningSwitch, frameChangeThresholdSlider, maxFrameChangeThresholdEntry, autoNoiseDetectSwitch, noiseLevelSlider. 596 passed.
- `enh/login-enable-reboot` (Fixes #1290, `7164ddf6`): `GET /login` also returns `enable_reboot` (`settings.ENABLE_REBOOT`); test `test_get_login_tells_whether_the_power_buttons_are_enabled` for both values. 597 passed.

#3553 approved by MichaIng (2026-11-13): setlocale only affects Python's locale-aware formatting (strftime for notifications), not subprocesses or translations; nothing to do.

#3554 review (MichaIng, 2026-11-14, comment edited once): bare value for `listen` only; `LISTEN = ''` default; sample line commented ("a `listen` key without value looks weird"). Done in 7e9a0770 (MichaIng co-author): meyectl accepts a bare line only for LISTEN, settings default '', sample `#listen 0.0.0.0` with the three alternatives; tests: default '', bare line, `media_path` without value still fails. 3.9: 601 passed, ruff/mypy/format/shellcheck clean. Pi 5: commented line → 0.0.0.0:8765 + [::]:8765, PC over IPv6 and IPv4 200, 127.0.0.1 200; existing `listen 0.0.0.0` → IPv4 only. PR retitled "feat(settings): listen on all IPv4 and IPv6 addresses by default", body rewritten, reply posted (issuecomment-6866995934, notes that new installs listen on the global IPv6 address). Pi restored to #3546 head (918ec330) with its conf.

2026-11-14: #3546 merged (9df56edd; closed #2425, #2683, #2812 with v0.45.0) and #3553 merged (565229e4; #2952 closed, v0.45.0). feat/libcamerify and fix/unsupported-locale deleted locally and on the fork, their commits abandoned; 9 branches rebased onto dev 565229e4 without conflicts and pushed. #3554 rebased (0826255e): 3.9 ruff/format/mypy clean, 614 passed, shellcheck clean; MERGEABLE, APPROVED by MichaIng (he resolved his own thread "fine as it is"; replied on the IPv6 note that most NATs block it, no change asked). Open follow-ups: wiki Troubleshooting update for libcamera_v4l2 (memory wiki-after-3546); close the libcamera issues that waited for #3546 (#2804, #2917, #3022, #3046, #3116, #3183, #2707; #2900 is Motion's zombie fix, 4.7.0 recommended).

2026-11-14: wiki Troubleshooting updated after #3546 (wiki 7260c47): "motionEye 0.45.0 and later" (motioneye_init --libcamera, or libcamera_v4l2 by hand; limits: other V4L2 cameras lose controls and get libcamera names, common resolution list while motion uses a camera; motion >= 4.7.0 recommended), "motionEye 0.44.0 and earlier" keeps the libcamerify steps, "Choosing the camera device" heading. Rendered headings checked on GitHub. Memory note for this task removed.

2026-11-14: `fix/picture-dialog-load` → **submitted as [#3555](https://github.com/motioneye-project/motioneye/pull/3555)** (d1525dbe on dev 565229e4; 609 passed; labels bug, JavaScript; v0.45.0; Fixes #2214). `fix/threshold-tuning-order` → **submitted as [#3556](https://github.com/motioneye-project/motioneye/pull/3556)** (b11f13fc; 609 passed; labels bug, HTML/HTTP; v0.45.0; Fixes #1349) with before/after screenshots: two Docker trixie containers (dev and branch, MJPEG test camera) on 18766/18767, Playwright 1.65.1 via mise node with the installed chromium-1248 (`executablePath`), 2x scale, clipped to the Motion Detection title and its first four visible rows; note the "please set a password" OK already opens the settings, so the menu button must not be clicked again. Uploaded as GitHub attachments by pasting into the PR comment box (cleared, not submitted); fork branch pr-1349-assets deleted afterwards. Script: scratchpad pw/shot.mjs.
