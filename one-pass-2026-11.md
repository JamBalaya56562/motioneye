# One-pass triage of open issues (from 2026-11-09)

Each open issue is read once to decide its labels and close/keep together (user, 2026-11-09). Order: the last comment of someone other than us and bots (our labelling moved `updated_at`). Batches of ~25, read by 3 read-only agents; close evidence rechecked on dev by me. Closes ~5 a day, each OKed. Issues that need the Pi wait until the user is home.

Also adopted: duplicate clusters under one canonical issue, an issue-template PR (`.github/ISSUE_TEMPLATE` does not exist), and fix PRs for bugs that reproduce on dev.

## Batch 1 (last human comment 2016-04 .. 2017-03, dev `71c81138`)

### Closed 2026-11-09 (user OK)

| # | Reason | Labels added | Evidence |
|---|---|---|---|
| #200 | completed | — | Clean Cloud switch, `main.html:450`, since 0.40 (PR #1118, linked under Development; no milestone, older than 0.43.1) |
| #271 | completed | — | `POST /action/<id>/snapshot`, `eventstart`/`eventend`: `server.py:219`, `action.py:64`. snapshot action since 2015 (`0dd3b683`, no PR); eventstart/eventend by PR #3468, linked, milestone v0.45.0 |
| #184 | not planned, duplicate of #232 | duplicate | Delete all exists; selective delete is #232 |
| #214 | completed | motion, Raspberry Pi, legacy motionEye | cron answer, reporter would try it, no follow-up since 2016 |
| #340 | completed | motion, Raspberry Pi, legacy motionEye | Motion-side (Motion-Project/motion#246), fixed with newer Motion |

### Closed 2026-11-09, second set (user OK, read in full by me)

| # | Reason | Labels added |
|---|---|---|
| #388 | not planned, duplicate of #192 | duplicate |
| #423 | not planned | motion, Raspberry Pi, legacy motionEye |
| #320 | not planned | motion, legacy motionEye |
| #363 | not planned | motion, legacy motionEye |
| #401 | not planned | Raspberry Pi, legacy motionEye (no motionEyeOS: cause not shown to be there) |

### Closed 2026-11-09, third set (user OK, read in full by me)

| # | Reason | Labels added |
|---|---|---|
| #385 | not planned | external bug, Raspberry Pi, legacy motionEye |
| #335 | not planned | Raspberry Pi, legacy motionEye |
| #228 | not planned | legacy motionEye |
| #439 | not planned (answered by the current UI) | none (motion dropped from the proposal; no legacy, answered on current UI) |
| #315 | not planned | Raspberry Pi, legacy motionEye |

### Keep (label changes applied 2026-11-09, user OK)

- No change: #142, #279, #232, #413, #192
- #165 feature → enhancement (HEAD exists, `handlers/base.py:295`; Content-Type of HEAD on pictures still missing, unverified at runtime)
- #277 feature → enhancement, +motion; #179 +motion; #258 +Raspberry Pi; #190 +motion (no overlay in recordings, so kept)

Clusters: bulk delete (#232 ← #184), pause all cameras (#192 ← #388), bulk download (#279). Unverified: whether the "One Picture" still is attached to the notification email (#363/#277).

## Batch 2 (last human comment 2017-02 .. 2017-09, dev `71c81138`)

Type and topic labels applied 2026-11-09 (user asked for the labelling). `legacy motionEye` and `duplicate` are added only on close.

### Keep

| # | Labels now | Note |
|---|---|---|
| #338 | feature, motion | no camera-lost notification; email text fixed in `sendmail.py:38` |
| #287 | feature, motion | Motion timelapse movies only via Extra Motion Options |
| #302 | feature | canonical: delete oldest media when the disk fills; cleanup is age-based (`mediafiles.py:448`). Duplicate candidates #1074, #897, #1981 (titles only, read before closing) |
| #446 | feature | MQTT: no `mqtt` in the code |
| #562 | feature | hover preview of movies |

### Closed 2026-11-09, fourth set (user OK, read in full by me)

| # | Reason | Labels added / Development |
|---|---|---|
| #529 | completed: one-picture mode (0.37) | none; PR #616 linked, no milestone (pre-0.43.1) |
| #592 | completed: same | none; PR #616 linked |
| #445 | not planned, duplicate of #2379 | duplicate, legacy motionEye |
| #659 | not planned, duplicate of #1223 | duplicate, legacy motionEye |
| #273 | not planned, duplicate of #251 (mentions `detectionstart` / `detectionpause` from #3468, auth needed) | duplicate, legacy motionEye |

### Closed 2026-11-09, fifth set (user OK, read in full by me)

All not planned, `legacy motionEye` added, no PR to link.

| # | Reason |
|---|---|
| #330 | Motion 4.0 fast playback, fixed by Motion-Project/motion#431 (merged 2017-07-30, checked via API) |
| #567 | same cause as #330 |
| #419 | Python 2 Jinja2 byte-compile warnings, upgrade worked; `requires-python >= 3.9` now |
| #516 | USB bandwidth (lower resolution fixed it for another user) |
| #538 | Motion gives no per-frame changes; only "Show Frame Changes" (`text_changes`) |

### Closed 2026-11-09, sixth set (user OK, read in full by me)

All not planned, `legacy motionEye` added, no PR to link.

| # | Reason |
|---|---|
| #576 | D-Link connection lost, no logs, no follow-up |
| #609 | movies do not play, Pi Zero W, no details |
| #642 | notifications never fire, no details |
| #640 | low fps on Pi Zero, Raspbian 8, logs expired |
| #479 | answered; remaining problem was the 2017 motionEyeOS image (motionEyeOS label kept) |

### Pi check (deferred until the user is home)

- #443: mask with 90/270 rotation is not applied to detection (follow-up of #437, after 43288b2). Rotate the camera, draw a mask, check that motion ignores the masked part on dev. Kept open until then.
  - Checked 2026-11-09 on the Pi 5 (Camera Module 3, Motion 4.7.1) with dev `71c81138` (0.45.0b1), set through `motion_camera_dict_to_ui` → `motion_camera_ui_to_dict` → `set_camera` (what `/config/1/set/` calls), as no session login was used. 640x480, left half of the shown picture masked, threshold 30 px and noise level 3 so that camera noise starts events, debug pictures on, 40 s per case. Bright pixels per half (every 2nd px):
    - 90°, no mask: left 38400 / right 38400
    - 90°, mask: left 0 / right 38400; `mask_1.pgm` is 480x640; no size warning in motion.log
    - 270°, mask: left 0 / right 38400
    - 0°, mask: left 0 / right 38400 (640x480)
    - Read back for the editor at 90°: `[480, 640]`, 42 rows, all `0xffff0000`
  - Works on dev. Closed 2026-11-09 as completed (user OK), no PR or milestone, labels unchanged. Pi restored: config from `~/meye-backup-20261109`, motionEye fork `ef1c1440` (0.45.0a1) reinstalled.
- #319 closed by mistake on 2026-11-09 as completed: README log 2026-11-07 says `rotate 90` at 640x480 still gives a 480x640 stream on Motion 4.7.1, against the reporter's "implemented". Reopened 2026-11-09 without a comment (user); the user deletes the wrong close comment.

### Closed 2026-11-09, seventh set (user OK, read in full by me)

All not planned, `legacy motionEye` added, no PR to link. Batch 2 close list is done.

| # | Reason |
|---|---|
| #400 | answered: Motion encodes via ffmpeg libs; UI offers H.264/OMX and V4L2M2M (`templates/main.html:795`) |
| #610 | each new file is uploaded on save (`handlers/relay_event.py:105`, `:110`); no sync of existing files |
| #666 | USB camera in a VM, same camera worked on a Pi |
| #195 | systemd `RequiresMountsFor=<path>`; missing mount only logs an error now (`config.py:1912`, boot behaviour unverified) |

Batch 2 result: 5 kept, 20 closed (#443 after the Pi check).

## Batch 3 (open.json rows 50-74, last human comment 2017-09 .. 2018-03, dev `71c81138`)

All 25 read in full by me on 2026-11-09.

### Keep

| # | Labels | Note |
|---|---|---|
| #675 | enhancement | global defaults for all cameras |
| #679 | bug | fullscreen with fit frames + rows > 1; not rechecked on dev UI yet |
| #676 | enhancement | lower stream rate to the browser without motion |
| #704 | enhancement | no current / retype password fields in `templates/main.html` |
| #708 | enhancement | canonical: upload retries; `uploadservices.py` retries only auth (401) |
| #715 | feature | notify on login |
| #771 | enhancement | sliders use mouse events only (`static/js/ui.js:158`); fix-PR candidate with pointer events (dragging on touch inferred, not run) |
| #789 | feature | animated GIF previews |
| #814 | enhancement | movie preview is taken at a pre_capture offset (`mediafiles.py:524`), not the best frame |

### Closed 2026-11-09, batch 3 first set (user OK)

| # | Reason | Added |
|---|---|---|
| ~~#319~~ | closed by mistake, reopened (see Pi check) | — |
| #778 | completed (S3 part) | PR #1063 linked, milestone v0.43.1 |
| #671 | not planned: needs automount | legacy motionEye |
| #660 | not planned: local first; `smb_shares` for a network share | legacy motionEye |
| #646 | not planned: power supply | Raspberry Pi, legacy motionEye |

### Closed 2026-11-09, batch 3 second set (user OK)

| # | Reason | Added |
|---|---|---|
| #678 | not planned: RTSP lag over the internet, no reply | legacy motionEye |
| #692 | not planned: Motion's `auto_brightness`, no reply | motion, legacy motionEye |
| #691 | not planned: answered, no follow-up | legacy motionEye |
| #700 | not planned: question answered | Raspberry Pi, legacy motionEye |
| #722 | not planned: no details | legacy motionEye |

### Closed 2026-11-09, batch 3 third set (user OK)

| # | Reason | Added |
|---|---|---|
| #294 | not planned: Python 2 install script, obsolete | legacy motionEye |
| #772 | not planned: Motion decides; mask / best image | motion, legacy motionEye |
| #787 | not planned: Ansible role shared, nothing to do | legacy motionEye |
| #767 | not planned: internet path, no follow-up | legacy motionEye |
| #806 | not planned: GDrive at service start, no news | legacy motionEye |

### Closed 2026-11-09, batch 3 fourth set (user OK)

#302 (remove old files before the disk is full) stays open as the canonical issue:
not on dev (`grep quota|disk_usage|free_space|statvfs` finds only the usage display
and the migration check), no PR. Related: #897, #978, #1074, #1981 closed here;
#1328 and #1354 (loop recording) to propose next.

| # | Reason | Added |
|---|---|---|
| #808 | not planned: `.nomedia` script workaround, no news | legacy motionEye |
| #897 | not planned: duplicate of #302 | duplicate |
| #978 | not planned: duplicate of #302 | duplicate |
| #1074 | not planned: duplicate of #302 | duplicate |
| #1981 | not planned: duplicate of #302 (per-camera) | duplicate |

### Closed 2026-11-09, batch 3 fifth set (user OK)

| # | Reason | Added |
|---|---|---|
| #1328 | not planned: duplicate of #302 (loop recording) | duplicate |
| #1354 | not planned: duplicate of #302; UI move left for a new issue | duplicate |

Batch 3 close candidates done; #302 kept open as the canonical issue.
