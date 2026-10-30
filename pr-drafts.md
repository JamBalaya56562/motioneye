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

## `fix/mask-conf-path` — write mask files to the configured conf_path

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

## `fix/mask-grid` — build the mask editor grid at the capture size

- Branch: `JamBalaya56562:fix/mask-grid` (`eda341ae`), base `dev` (`5dc324ed`)
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

## enh/layout-columns-per-browser (takes over #1570)

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

## `enh/venv` — install into a venv (#3066)

- Branch: `JamBalaya56562:enh/venv` (`699081c1`), base `dev` (`7093e67d`)
- Fixes #3066; follows MichaIng's plan there (2024-10-19, 2026-02-22: `--meyectl`-like option for `linux_init`, passed by `motioneye_init`)
- Verified: 5 scenarios in a systemd Debian 13 container (2026-10-28), fork CI green on `f39efa29` (test_install 6/6, pre-commit); 439 passed on `699081c1`
- **Not verified**: the venv install on the real Pi (Pi 5, trixie). Can be run over `ssh raspi` before submitting (disposable)
- Labels to set: `documentation`, `Python`, `CI/CD`

**Title:** `feat(install): install into a venv, with the meyectl path passed by motioneye_init`

**Body:**

````
Fixes #3066

Recent Debian and Ubuntu versions do not allow `pip` to install outside of a venv, so the README worked around it with `break-system-packages` and `get-pip.py`. Simply installing into a venv was not enough: `linux_init` looks for `meyectl` in `/usr/local/bin` and `PATH`, where a venv's `bin` is not, so the systemd service failed to start (`ERROR: meyectl executable has not been found`, `status=203/EXEC`).

As suggested in https://github.com/motioneye-project/motioneye/issues/3066#issuecomment-3940839716:
- `linux_init` gets a `--meyectl PATH` option, used for `ExecStart` in place of the detection. A missing path, a directory or a missing argument aborts before anything is installed.
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

- `tests/test_motioneye_init.py` (new): `--meyectl` is passed when the environment has `meyectl`, and nothing otherwise.
- `test_install` on my fork: all six jobs passed.
- shellcheck as in CI: no warnings. `pytest`: 439 passed.

Side note, not changed here: `motioneye_init` exits with 0 even when `linux_init` fails, as on `dev`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `fix/smb-keep-file` — stop at the target dir when removing empty folders, without .keep (#1810)

- Branch: `JamBalaya56562:fix/smb-keep-file` (`e8e44128`), base `dev` (`7093e67d`)
- Fixes #1810; answers MichaIng's question there (2024-07-31) on why `.keep` was needed
- Verified: repro as `nobody` in a container (dev: target dir and its parent removed without `.keep`; read-only `.keep` → `[Errno 13] Permission denied: '…/.keep'`, file kept; branch: both fine). New tests fail on dev, each run alone; 443 passed; ruff OK
- Real SMB (2026-10-30, Docker: Samba 4.17.12 server, Linux 7.0 linuxkit CIFS client, mounted as motionEye does, target dir = mount root): **#1810 did not reproduce on dev** over SMB 2.1, 3.0, 3.1.1 with default Samba (`hide dot files = yes`, `.keep` gets attributes HA), `map hidden`/no `store dos attributes`, `hide files = /.*/`, or read-only create mode — overwriting the hidden `.keep` worked. The branch works on all of them (subfolders removed, mount root kept, an existing `.keep` left alone)
- **Not verified**: SMB 1.0 and 2.0 — the Docker Desktop kernel refuses them (`vers=2.0 mount not permitted when legacy dialects disabled`). The report (motionEyeOS 2020) and dariodoc's fix (switching from SMB1 to 3.x) point to SMB1. Next: try SMB 1.0 from the Pi (`ssh raspi`), whose kernel may allow it, against a Samba container or the Pi itself
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

On a real SMB share (Samba 4.17 server, Linux CIFS client mounted as motionEye does it, the target dir being the mount point), over SMB 2.1, 3.0 and 3.1.1: this branch removes the emptied folders and keeps the mount point, and leaves an existing `.keep` alone. With these dialects I could not reproduce the error itself: overwriting the hidden `.keep` worked, also with `map hidden` or `hide files`. The report (2020) and the comment that switching from SMB1 to 3.x helped point to SMB1, which my test kernel does not allow; the error above was imitated with a read-only `.keep`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
````

## `enh/remember-me` — bring back "remember me" (#3364)

- Branch: `JamBalaya56562:enh/remember-me` (`a806e6b2`), base `dev` (`7093e67d`)
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
