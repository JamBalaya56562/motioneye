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

## Batch 4 (open.json rows 75-99; #978 already closed in batch 3)

### Keep

| # | Why | Labels |
|---|---|---|
| #825 | multiple users + login log; still admin + normal only (`config.py:349`) | feature |
| #852 | webhook HTTP PUT; only GET/POST (`main.html:526`); fix-PR candidate | enhancement |
| #877 | `mosquitto-clients` not in the Docker image (`docker/Dockerfile:19`) | enhancement, +docker |
| #884 | custom favicon | feature |
| #833 | Google Drive upload falls behind; tasks still one thread (`tasks.py:29`) | troubleshooting |
| #926 | invert mask, not there | feature |
| #944 | `on_event_start` with detection off; `pause` set from `@motion_detection` (`config.py:656`), Pi check | troubleshooting |

### Closed 2026-11-09, batch 4 first set (user OK)

| # | Reason | Added |
|---|---|---|
| #824 | not planned: FTP stops, no log, no reply | legacy motionEye |
| #837 | not planned: same picture on two cameras, no details | legacy motionEye |
| #826 | not planned: lens hood, answered | legacy motionEye |
| #842 | not planned: `on_camera_lost` via Extra Motion Options (`config.py:2144`) | motion, legacy motionEye |
| #859 | not planned: GDrive second camera, no reply | legacy motionEye |

### Closed 2026-11-09, batch 4 second set (user OK)

| # | Reason | Added |
|---|---|---|
| #840 | not planned: low FPS, hints helped (8-12 fps) | Raspberry Pi, legacy motionEye |
| #804 | not planned: power (IR, PIR, GSM modem) | Raspberry Pi, legacy motionEye |
| #892 | not planned: board comparison question, 2018 | Raspberry Pi, legacy motionEye |
| #899 | not planned: size from scene / Movie Quality / passthrough | legacy motionEye |
| #923 | not planned: Pi Zero software encoding; V4L2M2M | Raspberry Pi, legacy motionEye |

### Closed 2026-11-09, batch 4 third set (user OK)

| # | Reason | Added |
|---|---|---|
| #917 | not planned: frame from relayed events, not for Simple MJPEG; one cause fixed in #3469 | legacy motionEye |
| #936 | not planned: network camera, no log | legacy motionEye |
| #958 | not planned: HEVC in software on Pi 3 | Raspberry Pi, legacy motionEye |
| #933 | not planned: like #946 (client reload), no news | legacy motionEye |
| #968 | not planned: 16 RTSP cameras on a Pi 3B+ | Raspberry Pi, legacy motionEye |

### Closed 2026-11-09, batch 4 fourth set (user OK)

| # | Reason | Added |
|---|---|---|
| #967 | completed: eventstart/eventend action (`handlers/action.py:64`) | PR #2691 linked, milestone v0.45.0 |
| #974 | not planned: no RTC, system clock | Raspberry Pi, legacy motionEye |

Batch 4 done: 7 kept, 17 closed.

## Batch 5 (open.json rows 100-124; #1074 already closed in batch 3)

### Keep

| # | Why | Labels |
|---|---|---|
| #565 | mask file + smart mask together; still one type (`config.py:1420` if/elif) | enhancement |
| #1020 | multi-select in the media browser, not there | feature |
| #1058 | picture/movie counts in the camera bar | feature |
| #972 | API; ccrisan would take PRs | feature |
| #1057 | Captured Before with emulate_motion; Pi check whether `eventstart` keeps pre_capture | external bug |

### Closed 2026-11-09, batch 5 first set (user OK)

| # | Reason | Added |
|---|---|---|
| #982 | not planned: streams decoded twice (VLC + Motion) | legacy motionEye |
| #987 | not planned: details not given | legacy motionEye |
| #988 | not planned: answered, Motion analyses frames | Raspberry Pi, legacy motionEye |
| #994 | not planned: motionEyeOS feature, covered there | legacy motionEye |
| #995 | not planned: publish 8081 (`docker/docker-compose.yml:11`) | docker, legacy motionEye |

### Closed 2026-11-09, batch 5 second set (user OK)

| # | Reason | Added |
|---|---|---|
| #1040 | completed: "Remove Files After Upload" (`@clean_uploaded`) | PR #3374 linked, milestone v0.45.0 |
| #1013 | not planned: duplicate of #814 | (duplicate already) |
| #1076 | not planned: duplicate of #877 | duplicate, docker |
| #1045 | not planned: page without stylesheet on one phone | legacy motionEye |
| #1061 | not planned: image built for arm64/armv7 (`.github/workflows/docker.yml:63`) | docker, Raspberry Pi, legacy motionEye |

### Closed 2026-11-09, batch 5 third set (user OK)

| # | Reason | Added |
|---|---|---|
| #1029 | not planned: diagnosis not reported | legacy motionEye |
| #540 | not planned: answered | legacy motionEye |
| #664 | not planned: forward the streaming port, answered | legacy motionEye |
| #1075 | not planned: Pi 3B+ load, no log | Raspberry Pi, legacy motionEye |
| #1113 | not planned: action button files `<action>_<camera_id>` (`config.py:2200`) | legacy motionEye |

### Closed 2026-11-09, batch 5 fourth set (user OK)

| # | Reason | Added |
|---|---|---|
| #1114 | not planned: Pi 1, use the sub-stream (answered) | Raspberry Pi, legacy motionEye |
| #1121 | not planned: `stream_localhost` (`config.py:1126`); picture URL needs login (`handlers/picture.py:185`) | legacy motionEye |
| #921 | not planned: `POST /action/<camera_id>/<action>` (`server.py:219`); full API in #972 | legacy motionEye |
| #1133 | not planned: DISPLAY/XAUTHORITY for root (answered) | Raspberry Pi, legacy motionEye |

Batch 5 done: 5 kept, 19 closed.

## Pi check 2026-11-09 evening (#944, #1057)

Pi 5 + Camera Module 3, Motion 4.7.1, motionEye dev 71c81138 (0.45.0b1) installed for the
test; config backed up to `~/meye-backup-20261109b`, then restored and ef1c1440 reinstalled.
Settings were changed with the same functions as `/config/1/set/` (`motion_camera_ui_to_dict`
+ `set_camera`). Motion logs to syslog (journal) here, not `motion.log`.

### #944: `on_event_start` with motion detection off

Threshold 0.01 %, noise level 1, 45 s run, `on_event_start` command appends to a file:

| motion_detection | `pause` in camera-1.conf | `/1/detection/status` | on_event_start calls |
|---|---|---|---|
| on | off | ACTIVE | 2 |
| off | on | PAUSE | 0 |

Fixed by PR #3372 (0.45.0b1): motion starts with `pause on` instead of a webcontrol request
at startup that could come before motion was ready. Closed 2026-11-09 (user OK): completed,
PR #3372 linked, milestone v0.45.0. Labels: +bug, -troubleshooting (cause found).

### #1057: Captured Before with emulate_motion / eventstart

10 fps, post_capture 0, threshold 50 % (no natural events), 5 s event via webcontrol;
movie format `mp4` (Pi 5 has no `h264_v4l2m2m` encoder: "ffmpeg_set_codec" error).
ffprobe frames / seconds of the triggered movie:

| trigger | pre_capture 0 | pre_capture 30 |
|---|---|---|
| `/1/action/eventstart` | 51 / 5.0 s | 80 / 7.9 s |
| `/1/config/set?emulate_motion=1` | 50 / 4.9 s | 81 / 8.1 s |

About 30 more frames with Captured Before in both ways, so Motion 4.7.1 honours it.
Closed 2026-11-09 (user OK): completed, no motionEye PR, no milestone. Labels: +motion.

## Label corrections (since 2026-11-09)

The user's rule: remove wrong labels too, on every closed issue; never leave zero labels
(placeholder `troubleshooting` was added only to avoid that). `troubleshooting` stays where the
cause was never found; it goes where the close established it.

Batch 3-5 closes of 2026-11-09:

| # | Change | Why |
|---|---|---|
| #691 | -troubleshooting, +question | answered: separate folders for movies/pictures |
| #692 | -troubleshooting, +question | answered: switch is Motion's `auto_brightness` |
| #899 | -troubleshooting, +question | answered: size from scene / quality / passthrough |
| #958 | -troubleshooting, +question | cause: no HEVC hardware encoder on Pi 3 |
| #1114 | -troubleshooting, +question | answered: sub-stream on a Pi 1 |
| #1121 | -troubleshooting, +question | works as intended (`stream_localhost`) |
| #921 | -feature, +question | answered: action URL exists; API request is #972 |
| #944 | -troubleshooting, +bug | cause found and fixed by #3372 |
| #1057 | +motion | Motion behaviour |

Still to review: 312 issues closed by JamBalaya56562 before 2026-11-09 and the 2026-11-09
batch 1-2 closes (list from the closed-issue search, closer = JamBalaya56562: 406 in all).

### Review 1 (closes of 2026-10-25 to 2026-10-31, 25 issues; user OK)

Order: `lbl_todo` = issues closed by JamBalaya56562, by close date, batch 3-5 of 2026-11-09 left out.

| # | Change | Why |
|---|---|---|
| #657 | -Raspberry Pi | reporter's server is behind nginx, no Pi |
| #1459 | -Raspberry Pi | reporter on Ubuntu Server |
| #2232 | -question | wiki change proposal, documentation only |
| #2778 | -question, -legacy motionEye, +feature | Python 3 support, shipped in 0.43.1 (PR #3242) |
| #1408 | -question | Chrome 76 broke UI streaming: external bug |
| #2034 | -feature | limit of existing action buttons: enhancement |

Unchanged: #1497, #2828, #284, #353, #1094, #1356, #2746, #405, #3057, #1496, #2062,
#2083, #2792, #2934, #406, #1334, #2243, #2540, #1156.

### Review 2 (closes of 2026-10-31 to 2026-11-06, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #1265 | -troubleshooting, -Raspberry Pi, +bug | image lacked tzdata, fixed; reporter on a Proxmox VM |
| #3255 | -question | libcamera bug (fixed in 0.7) |
| #3269 | -question, +enhancement | arm64 image, Sponsored OSS, README: requests, all done |
| #3364 | -question, -documentation, +enhancement | "remember me" replacement via #3410/#3515 |
| #2625 | -docker | reporter not on Docker (a commenter was) |
| #2802 | -docker | reporter used pip2 |
| #3233 | -troubleshooting | cause found, fixed by #3520 |
| #2125 | -troubleshooting | reporter said it works |
| #2585 | -bug, +Raspberry Pi | old Python 2 install vs Bullseye libcurl; Raspbian |
| #2784 | -bug | botocore + urllib3 2, outside motionEye |

Unchanged: #2799, #2869, #2798, #3056, #1240, #2763, #3080, #3029, #3053, #3369, #2957,
#3026, #3059, #2465, #2684.

### Review 3 (closes of 2026-11-06 to 2026-11-07, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #256 | +Raspberry Pi | reporter on a Pi (`pi@webcam01`) |
| #308 | -external bug | ffmpeg not installed right, a setup answer |
| #327 | -troubleshooting, +question | cause found: USB 2.0 bandwidth |
| #345 | -troubleshooting, +question | mask worked as set; later a corrupted data partition |
| #411 | -troubleshooting | cause found: ffmpeg build without the mp4 codec |
| #459 | -troubleshooting, -docker, -motionEyeOS | Motion 4.0.1, fixed in 4.1; reporter used pip |
| #487 | -external bug | cause never found |
| #495 | -Home Assistant addon | reporter on motionEyeOS; HA ffmpeg component was a commenter |
| #514 | -docker | Docker was a later commenter |

Unchanged: #2906, #170, #262, #289, #306, #307, #317, #357, #358, #381, #414, #428, #442,
#449, #465, #501.

### Review 4 (closes of 2026-11-07, 25 issues; user OK)

From here on, labels that are only uncertain (e.g. `external bug` where Motion, ffmpeg or the
kernel is the likely cause) stay, as label-scheme says to label more when unsure; only clearly
wrong ones go.

| # | Change | Why |
|---|---|---|
| #539 | -troubleshooting, +question, +motion | solved via streameye; Motion's Pi camera handling |
| #595 | -troubleshooting, +question | answered: upload queue and folder |
| #608 | -troubleshooting, -Raspberry Pi | cause found (old MarkupSafe); reporter on OMV / Debian 8 |
| #637 | -external bug | router settings, not a bug |
| #669 | +Raspberry Pi | motionEyeOS on a Pi on a boat |
| #686 | -Raspberry Pi | problem on a headless server in Docker |
| #706 | -troubleshooting, +question | log showed ffmpeg could not be started |

Unchanged: #521, #526, #535, #546, #554, #558, #638, #639, #641, #645, #670, #690, #693,
#716, #717, #728, #735, #743.

### Review 5 (closes of 2026-11-07, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #818 | -troubleshooting, +bug | relay used the admin password; fixed by #3332 |
| #857 | -troubleshooting | fixed by a newer Motion |
| #866 | -troubleshooting, +question | fixed with the settings from #743 |
| #867 | -troubleshooting, +question | Pi throttling (overheating) in the log |
| #872 | -external bug | stale pip cache, not a bug |
| #888 | -troubleshooting, +question | answered: "Video Streaming" setting |
| #922 | -troubleshooting, +question | URL was not a stream |
| #943 | -external bug | no ffmpeg package in that Raspbian |
| #950 | -motionEyeOS | reporter on Ubuntu Server; answer is a motionEye setting |
| #951 | -Raspberry Pi | reporter on a Debian 9.5 machine |
| #960 | -Raspberry Pi | Odroid XU4 |
| #1003 | -troubleshooting, -Raspberry Pi | cause found (4:4:4 profile); reporter on Lubuntu |

Unchanged: #747, #756, #768, #794, #803, #901, #902, #912, #916, #931, #952, #956, #957.
