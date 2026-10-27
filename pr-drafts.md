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
