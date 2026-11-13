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

### Review 6 (closes of 2026-11-07, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #1046 | -troubleshooting, +question | workaround known: enter `rtsp://<address>` first |
| #1206 | -Raspberry Pi | reporter on an Ubuntu VM |
| #1379 | -troubleshooting, -Raspberry Pi, +question | answered: credentials not in the URL; reporter on Docker amd64 |

Unchanged: #1010, #1025, #1052, #1067, #1089, #1092, #1232, #1236, #1256, #1257, #1268,
#1269, #1281, #1304, #1352, #1364, #1392, #1393, #1400, #1419, #1443, #1444.

### Review 7 (closes of 2026-11-07 to 2026-11-08, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #2244 | -troubleshooting | success report, no problem |
| #3527 | -troubleshooting | cause found, fixed by #3496 |
| #267 | -troubleshooting | log showed Motion exiting on an RTSP 401 |
| #603 | -troubleshooting, +question | SMTP port / TLS mismatch |
| #782 | -troubleshooting, +question | solved by settings (slashes, subfolders) |

Unchanged: #1480, #1487, #1503, #1532, #1855, #1859, #2556, #2623, #2630, #2834, #2858,
#2867, #2875, #3171, #3177, #3198, #3267, #3344, #575, #753.

### Review 8 (closes of 2026-11-08, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #871 | -troubleshooting, +bug | old ARM image base broken; fixed by a Raspbian base |
| #927 | -troubleshooting | Pillow built against libjpeg8 |
| #964 | -troubleshooting, -motionEyeOS, +enhancement | failed uploads are not retried (still so), a motionEye limit |
| #970 | -troubleshooting, +question | solved with Fast Network Camera + streaming URL |
| #976 | -troubleshooting, +question | camera interface not enabled in the OS |
| #985 | -troubleshooting, +question | `VIDIOC_S_INPUT: Device or resource busy` |
| #1002 | -legacy motionEye | done by PR #2353 (`User=motion`), in 0.43.1 |
| #1095 | -motionEyeOS | load of decoding five cameras, not motionEyeOS |

Unchanged: #820, #834, #868, #896, #900, #991, #992, #1006, #1012, #1014, #1050, #1056,
#1062, #1079, #1084, #1085, #1097.

### Review 9 (closes of 2026-11-08, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #1124 | -troubleshooting | Python 2 `smtplib`, CRAM-MD5 with a non-ASCII password |
| #1144 | -troubleshooting, +question | works as designed: JPEG per frame at the streaming rate |
| #1176 | -troubleshooting, -legacy motionEye, +enhancement | done by PR #2353 (`User=motion`), as #1002 |
| #1180 | -motionEyeOS | motionEye problem, fixed by #3468/#3506 |
| #1181 | -motionEyeOS | message is motionEye's upload queue limit |
| #1261 | -troubleshooting | fixed by Motion 4.3.2 |

Unchanged: #1111, #1117, #1122, #1123, #1128, #1131, #1141, #1146, #1169, #1174, #1183,
#1192, #1243, #1250, #1252, #1253, #1258, #1270, #1282.

### Review 10 (closes of 2026-11-08, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #1386 | -troubleshooting, +question | Motion 3.2.12 too old for motionEye 0.40's config |
| #1417 | -troubleshooting, +question | normal user cannot bind the port |
| #1481 | -troubleshooting, +question | log was Motion run alone with its defaults |
| #1492 | -motionEyeOS | reporter on Raspbian; answer is an OS mount |

Unchanged: #1291, #1305, #1331, #1344, #1347, #1350, #1387, #1420, #1427, #1433, #1439,
#1442, #1445, #1471, #1477, #1483, #1486, #1491, #1493, #1498, #1499 (`external bug` kept on
pycurl / Tornado build problems: label-scheme counts Python packages as external).

### Review 11 (closes of 2026-11-08, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #1504 | -troubleshooting, +question | setup found; commands run as Motion's user |
| #1643 | -motionEyeOS | reporter on Ubuntu Server; answer is `motioneye.conf` |
| #1894 | -question | feature request, privacy mask #1247 in 0.43.1 |
| #2015 | -troubleshooting | answered: movie length settings |
| #2017 | -enhancement, -question | new codec: feature only |
| #2022 | -troubleshooting | both solved on the camera side |
| #2038 | -troubleshooting, +question | Layout Columns hidden by the screen width |

Unchanged: #1505, #1524, #1528, #1799, #1808, #1834, #1842, #1848, #1857, #1863, #1867,
#1889, #2023, #2024, #2025, #2029, #2031, #2037.

### Review 12 (closes of 2026-11-08, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #2040 | -troubleshooting | solved with `--device /dev/vchiq` |
| #2042 | -troubleshooting, -question, -legacy motionEye | privacy mask #1247, in 0.43.1 |
| #2048 | -troubleshooting | the camera's RTSP stream (UDP smearing, TCP delay) |
| #2064 | -troubleshooting, +question | camera sleeping; new camera fixed it |
| #2069 | -troubleshooting | KC100 sends its own HTTPS stream, Motion cannot read it |
| #2091 | -troubleshooting | rsync from cron picks up files being written |
| #2146 | -troubleshooting | the lines do not come from motionEye |
| #2147 | -troubleshooting | permissions fixed via "Running As Normal User" |
| #2182 | -motionEyeOS | camera URL format, not motionEyeOS |

Unchanged: #2041, #2065, #2072, #2080, #2081, #2084, #2105, #2107, #2108, #2131, #2138,
#2145, #2151, #2153, #2175, #2068.

### Review 13 (closes of 2026-11-08 to 2026-11-09 batch 1, 25 issues; user OK)

| # | Change | Why |
|---|---|---|
| #2183 | -troubleshooting | fixed by `After=network-online.target`, checked |
| #2185 | -question, +enhancement | install suggestion, done in 0.43.1 (PR #2980) |
| #2186 | -troubleshooting | the 502 came from the add-on proxy (28765) |
| #2195 | -troubleshooting | settings question, answered |
| #2202 | -troubleshooting | motionEyeOS kernel sees no link |
| #228 | -troubleshooting, +bug | old slider snapping, sliders rebuilt |
| #273 | -legacy motionEye | duplicate of the open #251, as the #302 cluster |
| #330 | -troubleshooting | Motion bug, fixed in Motion-Project/motion#431 |

Unchanged: #2187, #2192, #2194, #2207, #2213, #2239, #2247, #184, #195, #200, #214, #271,
#315, #320, #335, #340, #363.

### Review 14 (closes of 2026-11-09 batch 1-2, last 21 issues; user OK)

| # | Change | Why |
|---|---|---|
| #385 | -external bug | failing USB camera or hub power: hardware |
| #419 | -troubleshooting, +question | only Jinja2 byte-compile warnings, upgrade worked |
| #439 | +legacy motionEye | 2017 report |
| #445 | -legacy motionEye | duplicate of the open #2379 |
| #516 | -troubleshooting, -external bug, +question | USB bandwidth, a hardware limit |
| #567 | -troubleshooting | Motion 4.0 fast playback, fixed in Motion-Project/motion#431 |
| #659 | -question, -legacy motionEye, +feature | duplicate of the open request #1223 |
| #666 | -troubleshooting, +question | VM USB passthrough; same camera worked on a Pi |

Unchanged: #388, #400, #401, #423, #479, #529, #538, #576, #592, #609, #610, #640, #642.

Label review of all 346 closes by JamBalaya56562 done (with the batch 3-5 corrections:
all 406 closes since 2026-06).

## Batch 6 (open.json rows 125-149, last human comment 2019-01 .. 2019-05, dev `71c81138`)

### Closed 2026-11-10, batch 6 first set (user OK)

| Issue | Reason | Labels | Link / milestone |
|---|---|---|---|
| #1242 | completed: webhooks send `User-Agent: motionEye` | feature | #3378, v0.45.0 |
| #1116 | completed: fast-play button (5×, next video) | feature | #1975, v0.43.1 |
| #1187 | completed: settings autofill off since 0.40 (8cb4e46e) | −troubleshooting +bug +legacy motionEye | none (0.40) |
| #1233 | completed: answered, Preserve Movies/Pictures | +legacy motionEye | none |
| #1152 | not planned: Banana Pi Pro Wi-Fi, motionEyeOS | +legacy motionEye | none |

### Still to decide

- Keep (not implemented on dev): #1158 lastmovie, #1244 robots.txt, #697 pixel threshold
  (slider is 0-20 %, only the max threshold is in pixels), #1227 netcam modulo 8 check,
  #1054 activity log, #1189 home mode, #1137 snapshot token, #1254 stream TLS, #1273 font,
  #1276 camera description, #1290 user type JSON, #788 brightness sensor.
- Batch 6 done: 13 closed, the other 12 are open feature requests, kept.

### Closed 2026-11-10, batch 6 third set (user OK, completed)

| Issue | Labels after | Note |
|---|---|---|
| #1145 USB capture card | question, +Raspberry Pi, +legacy motionEye | answered: UVC card = V4L2 camera |
| #1203 lighttpd reverse proxy | question, +legacy motionEye | answered: paths are relative since 0.36 (5ec72dc9), so the `/static/` requests come from `/meye` without a trailing slash; my first comment said absolute paths were the cause and was edited in place, the v0.36 milestone I set was removed |
| #1229 `%f` path on a network share | −troubleshooting, +question, +motion, +legacy motionEye | answered: `/media/motioneye_<server>_<share>_<user>` is motionEye's own SMB mount |

Also #1187 (batch 6 first set) got v0.40, which did not exist when it was closed.

### Closed 2026-11-10, batch 6 second set (user OK, all not planned)

| Issue | Labels after |
|---|---|
| #1135 high CPU with RTSP, Motion 4.2.1 | troubleshooting, +motion, +legacy motionEye |
| #1154 green frames from IP cams on a Pi 3B+ | troubleshooting, +Raspberry Pi, +motion, +legacy motionEye |
| #1155 motion detection at night | −troubleshooting, +question, +motion, +legacy motionEye |
| #1162 webhook stops after a while | troubleshooting, +legacy motionEye |
| #1239 jumpy stream, Docker on a Pi 3B+ | troubleshooting, +docker, +Raspberry Pi, +legacy motionEye |

## Milestones for older releases (2026-11-10, user OK)

- Due dates of the closed milestones set by the user: v0.43.1 = 2025-12-11, v0.44.0 = 2026-06-20
  (GitHub Release dates; PyPI got 0.43.1 only on 2025-12-27).
- Created 42 closed milestones v0.27 (#4) .. v0.42.1 (#45), one per final tag on PyPI, due date =
  PyPI upload date (equal to the tag commit date except v0.31.5, tag 2016-05-20, and v0.38.1, tag
  2018-02-06). None for 0.1-0.26 (before issue #1 on 2015-08-30, not on PyPI) or rc tags.
- API note: `due_on=YYYY-MM-DDT00:00:00Z` is stored as the previous day; `T12:00:00Z` keeps the date.
- Next: link merged PRs (76 merged before 2020-06-07) by the first final tag containing the merge
  commit, and issues whose fixing PR or commit is known.
- Done 2026-11-10 (user OK): milestones set on 73 merged PRs (first final tag containing the merge
  commit; #58, #64, #127, #137 have no merge commit on GitHub, so their head commit) and on the 19
  closed issues those PRs reference as closing. Verified by GraphQL: 92 of 92 match.
- Merged PRs left without a milestone (8): python2-only #2305, #2309, #2356, #2529, #2608, #2654,
  #2840, and #2838 (merged into master, commit no longer on any branch). #877 is open, so none.
- Not done: older issues closed by "fixes #N" in commit messages without a PR.
- Done 2026-11-10 (user OK): 30 more closed issues fixed without a PR, or by a PR merged after
  0.42.1, got milestones: from closing references of PRs merged later (8), close comments naming the
  fix version or commit (15), and commit messages or comments naming the fix (7); #1093, #864, #885
  and #2257 also linked to #1102, #1384, #1508 and #2346. Verified by GraphQL: 30 of 30. Left out:
  #3178, #3255, #356, and number clashes (#2, #152 from Bitbucket, #5 from Weblate).
  Only one issue (#3066, already v0.45.0) is recorded by GitHub as closed by a commit.
- Gap found by the user (#1729, closed by hand before PR #1914 merged): swept all 2,250 closed
  issues for "no milestone + merged closing-reference PR" and gave 20 the PR's milestone (19 ×
  v0.43.1, #2989 v0.44.0). Only #2230 is left (PR #2777, milestone 2021.11.2, another repo).

## Batch 7 (open.json rows 150-174, last human comment 2019-05 .. 2019-08, dev `71c81138`; #1328, #1354 already closed)

### Keep

Feature requests not on dev: #698, #1287, #1315, #1322, #1339, #1353, #1358, #1375; #1349 (the
Auto Threshold Tuning switch is still after the two thresholds), #1359 (manual snapshots switch is
still independent of Capture mode manual).

### Closed 2026-11-10, batch 7 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #1298 Exec format error on a Pi Zero W | not planned, no details | troubleshooting, +Raspberry Pi, +legacy motionEye |
| #1283 movies saved as .avi and .mp4 | not planned, camera and install gone | troubleshooting, +motion, +legacy motionEye |
| #477 multiple file storage | not planned, no reply | question, +Raspberry Pi, +legacy motionEye |
| #1300 grey image while frame rate runs | not planned, no details | troubleshooting, +legacy motionEye |
| #1336 movie format with least CPU | completed, answered (passthrough, V4L2M2M) | question, +motion, +legacy motionEye |

### Closed 2026-11-10, batch 7 second set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #1213 threshold below 0.1 % | not planned, duplicate of #697 | −question, +duplicate, +enhancement |
| #1326 Docker cannot write to /media/username | completed, map the path with `-v` | question, +docker, +legacy motionEye |
| #1330 cameras gone with Wi-Fi off | completed, open 127.0.0.1 on the Pi | question, +Raspberry Pi, +legacy motionEye |
| #1332 upload a snapshot when motion starts | completed, Motion Triggered (One Picture) + Upload Pictures (`relay_event.py:108`) | question, +motion, +legacy motionEye |
| #1374 100 % CPU with 26 RTSP cameras | completed, Motion decoding | −troubleshooting, +question, +motion, +docker, +legacy motionEye |

#1332: the first draft suggested fetching `/picture/<id>/current/` from Run A Command; that needs a
session or HMAC (`handlers/base.py:263`), so the posted answer uses picture upload instead.

Closed 2026-11-10 (user OK): #1381 completed, answered (8081 is Motion's stream, a remote motionEye
camera needs port 8765); labels −troubleshooting, +question, +Raspberry Pi, +legacy motionEye.

Kept for a Pi check: #1312 (Bearer token for a netcam). Motion 4.7 documents only `netcam_userpass`
for camera auth, but for `http://` URLs `netcam_params` goes to FFmpeg, whose http `headers` option
might carry `Authorization: Bearer`; test with a small token-checking server before closing.

Batch 7 done: 11 closed, 12 kept (feature requests and #1312).

## Batch 8 (open.json rows 175-199)

Kept: #1317, #766 (continuous recording with motion detection / schedule), #1466, #1475, #1355,
#1465, #1485, #1107, #1223 (open feature requests); #1418 and the rest wait for the next sets.

### Closed 2026-11-10, batch 8 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #1489 Docker base Ubuntu 18.10 EoL | completed, fixed by #1822 (Debian), linked, milestone v0.43.1 | CI/CD, +docker |
| #1289 cifs-utils in the Docker image | not planned, mount on the host | feature, +docker, +legacy motionEye |
| #1460 snapshot from the console | completed, `curl http://127.0.0.1:7999/1/action/snapshot` (`motionctl.py:316`) | question, +legacy motionEye |
| #1103 Dropbox / Google Drive upload | not planned, reporter used own script | troubleshooting, +legacy motionEye |
| #1457 UI error after router swap | not planned, no reply; port 7999 bind error = second Motion | troubleshooting, +legacy motionEye |

#1460: the curl path is what motionEye calls itself; not run against a real Motion.

### Closed 2026-11-10, batch 8 second set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #628 Dahua digest authentication | completed, answered (Motion 4.x digest, RTSP URL works) | question, +motion, +legacy motionEye |
| #1461 no motion detection at night | completed, answered (needs IR light) | question, +motion, +Raspberry Pi, +legacy motionEye |
| #1467 changed-pixel count as a value | completed, answered (`text_changes` is drawn by Motion) | question, +motion, +legacy motionEye |
| #1500 no image, ECONNREFUSED | not planned, no reply; motionEye could not reach Motion | troubleshooting, +legacy motionEye |
| #1509 segfault on Debian 9 | not planned, crash in Motion's camera thread | troubleshooting, +motion, +legacy motionEye |

#1418 (change settings by URL) waits: Motion's web control has `webcontrol_parms 0` (`config.py:2500`),
so settings cannot be changed through it.

### Closed 2026-11-10, batch 8 third set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #1447 momentary action button | completed, the script switches on, waits, off (`handlers/action.py:80`) | question, +legacy motionEye |
| #1454 PTZ on GPIO | completed, `up_1`/`down_1`/`left_1`/`right_1` scripts (`config.py:51`) | question, +Raspberry Pi, +legacy motionEye |
| #1476 Google Home on motion | completed, web hook to IFTTT / Home Assistant | question, +legacy motionEye |
| #1482 nginx `/cams/` shows welcome page | completed, `server_name` does not match the IP | question, +legacy motionEye |
| #1416 timelapse defaults | not planned, no details | question, +legacy motionEye |

#1482: "needs no base path" rests on motionEye's relative URLs; not tried behind nginx.

Closed 2026-11-10 (user OK): #1418 not planned, duplicate of #972 (API for changing settings; HMAC
peer auth since 0.44.0 is for motionEye peers, not a documented API), snapshot answered as in #1460;
labels −question, +duplicate, +feature.

Batch 8 done: 16 closed, 9 kept (feature requests). #2027 (API Access, question) is close to #972 and
can be looked at when its batch comes.

## Batch 9 (open.json rows 200-224)

Kept: #1519, #1125, #1527, #40, #850, #251, #773, #790, #941, #1846, #1850, #1864, #1451 (open
feature requests and bugs); #1523, #1255, #1658, #1302, #1414, #1849, #1852 wait for the next sets.

### Closed 2026-11-10, batch 9 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #1449 Chrome 76 shows no video | completed, duplicate of #1401, milestone v0.41 | bug, +duplicate, +motionEyeOS, +Raspberry Pi |
| #1845 action button from a gateway | not planned, duplicate of #972; run `/etc/motioneye/preset1_1` directly | −question, +duplicate, +feature, +motionEyeOS, +Raspberry Pi |
| #1520 Pi Zero camera on the Pi 2 | completed, Remote motionEye Camera (`main.js:3840`) | question, +Raspberry Pi, +legacy motionEye |
| #843 pictures not saved | completed, answered (Still Images, Root Directory) | −troubleshooting, +question, +legacy motionEye |
| #1051 100 % CPU recording RTSP | completed, answered (Motion decoding/encoding) | question, +motion, +docker, +legacy motionEye |

#1520: the steps follow the UI's camera type; not tried with two Pis.

### Closed 2026-11-10, batch 9 second set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #1523 remote camera: no streaming URL, not on 7999 | completed, by design (`main.js:2371`) | −troubleshooting, +question, +Raspberry Pi, +legacy motionEye |
| #1658 changing frame rate brings the camera back | not planned, no reply; saving restarts Motion | troubleshooting, +motion, +Raspberry Pi, +legacy motionEye |
| #1302 motion detection not triggering | not planned, no reply to jasaw | troubleshooting, +motion, +legacy motionEye |
| #1414 special character in text overlay | not planned, not reproduced | troubleshooting, +motion, +legacy motionEye |
| #1852 no feed with the Arch instructions | not planned, no reply | troubleshooting, +legacy motionEye |

#1523: the "no advanced settings" part was left out of the comment, its cause was not confirmed.

Closed 2026-11-10 (user OK):
- #1255 not planned, Motion reads enabled cameras all the time; switch the camera off (`config.py:662`)
  or stop the service; labels question, +motion, +docker, +legacy motionEye.
- #1849 not planned, no reply; the Arducam adapter switches one camera at a time (from Arducam's
  description, not tried); labels troubleshooting, +Raspberry Pi, +legacy motionEye.

Batch 9 done: 12 closed, 13 kept (feature requests and bugs).

## Batch 10 (open.json rows 225-249)

Kept: #1887, #1902, #1909, #1924, #1518, #1949, #122, #736, #1987, #1712, #1966, #37, #1816, #1441
(open feature requests); #1856, #1030, #1938, #2033, #2035, #2036 wait for the next sets.

### Closed 2026-11-10, batch 10 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2027 API Access | not planned, duplicate of #972 | −question, −troubleshooting, +duplicate, +feature |
| #1911 threshold % vs frame changes px | not planned, duplicate of #1441 | enhancement, −question, +duplicate |
| #1531 Ezviz C4S grey screen | completed, camera firmware V5.3.1 | question, +Raspberry Pi, +legacy motionEye |
| #1965 still image every 10 s | completed, answered (`picture_output` modes, hook script) | enhancement, −help wanted, question, motion, +legacy motionEye |
| #2020 balenaCloud write-up | completed, not an issue | −enhancement, −feature, +documentation, +legacy motionEye |

## Label audit of our closes (2026-11-10, user OK)

All 463 issues closed by JamBalaya56562 were checked against the label rules (`audit_rules.py`):
`help wanted` only on #1965 (removed); `legacy motionEye` after 2023-12-24 only on #2957 (0.42.1)
and #3267 (old Python 2 snap), both correct; old PR fixes with `legacy motionEye` (0.40-0.43.1)
correct.

Fixed:
- #1842: −legacy motionEye, −question, +feature (implemented by #3468, v0.45.0).
- One type label where two were set (mostly by starbasessd in 2020-21), kept the one matching the
  close: #1965 −enhancement (answered); #1981 −enhancement (feature, dup of #302); #2239 −question
  (feature, not planned); #2105 −troubleshooting (answered how-to); #2023, #2024, #2025, #2031,
  #2041, #2080, #2145, #2151, #2194, #2247 −question (cause not established).

13 closes with only `documentation` (12) or `CI/CD` (#1489): fine, both count as type labels (user, 2026-11-10).

### Closed 2026-11-10, batch 10 second set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #1856 Run A Command not called | not planned, no details | troubleshooting, +legacy motionEye |
| #1030 commands run only on restart | not planned, no reply (2018 Docker) | troubleshooting, +docker, +motion, +legacy motionEye |
| #1938 Arducam B0176 autofocus | not planned, Motion has no focus control (docs, not tried) | question, +motion, +Raspberry Pi, +legacy motionEye |
| #2036 4th camera shows the 1st | not planned, same streaming port (zagrim) | troubleshooting, +legacy motionEye |

Kept: #2033 (Google Drive uploads over ~100 MB) relabelled −question, +enhancement: the upload uses
`uploadType=multipart` with the whole file (`uploadservices.py:369`), which Google documents for
small files; large ones need a resumable upload. #2035 kept (cause unknown, two type labels to settle).

Batch 10 done: 9 closed, 16 kept.

## Batch 11 (open.json rows 250-274)

#897 in this range was already closed (2026-11-09). Kept for now: open feature requests; #2058,
#2101, #2102, #2066, #2137, #1915, #2135 wait for the next sets. #1897 (closed by MichaIng 2023-09-15:
the old Docker Hub images are replaced by the multi-platform GHCR images of #2361) got #2361 linked
and milestone v0.43.1.

### Closed 2026-11-10, batch 11 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2140 multi-platform Docker image | completed, fixed by #2361 (buildx), linked, milestone v0.43.1 | −enhancement, feature, docker |
| #2018 PTZ follows motion | completed, answered (`track_type 9`, `track_generic_move`) | −enhancement, −feature, question, +motion, +legacy motionEye |
| #2124 webcontrol camera numbers shift | not planned, duplicate of #1887 (`config.py:662`) | −question, +duplicate, +enhancement, motion |
| #2049 Imou Looc no stream | completed, working RTSP URL | −troubleshooting, question, +legacy motionEye |
| #2087 where the web UI files are | completed, `templates/main.html`, `static/` | question, +legacy motionEye |

### Closed 2026-11-10, batch 11 second set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2102 remote camera with the surveillance login | completed, Client Secret gives peer access; use MJPEG URLs | question, +legacy motionEye |
| #1915 why JPEG frames, not MJPEG | completed, `picture/<id>/current/` through motionEye (`main.js:5607`) | question, +legacy motionEye |
| #2058 Avacom M1060W | not planned, no reply to suggested URLs | question, −troubleshooting, +legacy motionEye |
| #2101 remote camera black in QNAP Docker | not planned, worked in an Ubuntu VM | −question, troubleshooting, +docker, +Raspberry Pi, +legacy motionEye |
| #2137 mail "key too short" | not planned, the server's key (error text assumed) | troubleshooting, +legacy motionEye |

Our comments on #1520, #2105 and #1381 said to add a Remote motionEye Camera with the admin login;
since 0.44.0 (#3332) the dialog asks for the remote's Client Secret (`main.js:3860`), so the three
comments were edited in place (user OK).

Closed 2026-11-10 (user OK): #2066 not planned, no reply; the stream plus Still Images and FTP
upload covers the goal; labels troubleshooting, +legacy motionEye. Kept #2135: the recording mode
lives only in `emulate_motion`, written only with Movies on (`config.py:1397`), so it resets.

Batch 11 done: 11 closed, 13 kept (#897 in the range was already closed).

## Batch 12 (open.json rows 275-299)

Kept: open feature requests (#2141, #2157, #2160, #2130, #2166, #2172, #2169, #2205, #2059, #2210);
#2148, #2149, #2154, #2063, #2163, #2201, #2214, #2217, #2225, #2236 wait for the next sets.

### Closed 2026-11-10, batch 12 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2162 streaming resizing has no effect on URLs | completed, UI frames only (`mediafiles.py:1166`) | question, +legacy motionEye |
| #2191 resizing not on port 8081 | completed, Video Streaming off = localhost only (`config.py:1126`, UI not tried) | question, +legacy motionEye |
| #2203 camera always on | completed, answered (Motion reads every frame) | question, +motion, +docker, +legacy motionEye |
| #2215 picture browser slow to open | not planned, duplicate of #40 | −question, −troubleshooting, +duplicate, +feature |
| #1382 OneDrive upload with rclone | completed, write-up | −question, +documentation, +legacy motionEye |

### Closed 2026-11-10, batch 12 second set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2201 four cameras on port 7999, three in the UI | completed, camera 0 is `motion.conf` (Motion docs, not tried) | question, −troubleshooting, +motion, +legacy motionEye |
| #2163 Firefox overloads the CPU | not planned, no answer (0.42.1) | −question, troubleshooting, +legacy motionEye |
| #2063 Eufy 2C goes grey | not planned, no answer | −question, +troubleshooting, +Raspberry Pi, +legacy motionEye |
| #2236 commands stop after a while (HA add-on) | not planned, no reply | troubleshooting, Home Assistant addon, +legacy motionEye |
| #2148 HQ camera at 3840x2160 | not planned, 0.42.1 on the legacy camera stack | question, +Raspberry Pi, +legacy motionEye |

### Closed 2026-11-10, batch 12 third set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2217 working hours past 23:30 on mobile | completed, fixed by #3277 (native time input), linked, milestone v0.44.0 | enhancement, −question |
| #2154 Chrome lazy images flag gone | completed, duplicate of #1401 (fixed in 0.41), milestone v0.41 | question, motionEyeOS, +duplicate, +legacy motionEye |
| #2149 hub cameras keep spinning | not planned, no answer | troubleshooting, +Raspberry Pi, +legacy motionEye |
| #2225 ONVIF zoom buttons | not planned, about the user's script (`config.py:2200`) | question, +legacy motionEye |

Kept #2214 (picture viewer slows down after 50-100 pictures, seen in Firefox and Edge).

Batch 12 done: 14 closed, 11 kept.

## Batch 13 (open.json rows 300-324)

#1981 in the range was already closed. Kept: open feature requests; #2216, #2281, #2283, #2296,
#2297, #823, #2303, #2336, #2304, #2372, #2378, #2394 wait for the next sets.

### Closed 2026-11-10, batch 13 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2224 pytz not listed as dependency | completed, fixed by #3464 (`zoneinfo`), linked, milestone v0.45.0 | −question, −troubleshooting, +bug, +dependencies |
| #1024 scheduled still captures | not planned, duplicate of #883 | duplicate, −enhancement, feature |
| #2277 view another motionEyeOS | completed, answered (remote camera types) | question, +legacy motionEye |
| #2263 motionEye on a Pi Zero 2 W | completed, answered (README venv) | question, −motionEyeOS, +Raspberry Pi, +legacy motionEye |
| #2365 motionEye vs motionEyeOS | completed, answered (MichaIng) | question, motionEyeOS, +Raspberry Pi, +legacy motionEye |

Open #883 relabelled: −duplicate, −enhancement (it is the issue the duplicates point to).

### Closed 2026-11-10, batch 13 second set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2216 hourly DNS lookups on motionEyeOS | not planned, motionEyeOS system | −bug, question, +motionEyeOS, +Raspberry Pi, +legacy motionEye |
| #2297 pantilthat in Docker | completed, install it in a derived image (`docker/Dockerfile:38`; I2C device assumed) | question, docker, +Raspberry Pi, +legacy motionEye |
| #823 camera unusable after reconnect | not planned, no reply (2018 motionEyeOS) | troubleshooting, +Raspberry Pi, +legacy motionEye |
| #2303 docker "failed to register layer" | not planned, command split by line breaks | troubleshooting, +docker, +Raspberry Pi, +legacy motionEye |
| #2304 Dahua RTSP slow over LTE | not planned, link and Pi Zero 2 W decoding | question, motion, +Raspberry Pi, +legacy motionEye |

Open #2378 (Google shared drives) relabelled −question, −troubleshooting, +enhancement: the parent
is fixed to `root` (MichaIng).

### Closed 2026-11-10, batch 13 third set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2281 motionEyeOS build for the Pi Zero 2 W | not planned, motionEyeOS | enhancement, motionEyeOS, +Raspberry Pi, +legacy motionEye |
| #2283 performance on the Pi Zero 2 W | completed, answered | question, +motionEyeOS, +Raspberry Pi, +legacy motionEye |
| #2296 set date and time from the UI | not planned, OS / motionEyeOS | −duplicate, −enhancement, −question, feature, +motionEyeOS, +Raspberry Pi, +legacy motionEye |
| #2336 cannot mount network share | not planned, no reply (0.42.1) | troubleshooting, +legacy motionEye |
| #2394 config restore fails | not planned, no details; restore reworked (#3338, #3341) | troubleshooting, +legacy motionEye |

Kept #2372 (Movie Passthrough starts too early).

Batch 13 done: 15 closed, 9 kept (#1981 in the range was already closed).

## Batch 14 (open.json rows 325-349)

Kept for now: open feature requests (#2414, #2441, #2442, #2473); #2417, #2419, #1484, #2448, #2433,
#2438, #2453, #2461, #2494, #1630, #2530, #1463, #2525, #2526, #1829, #2532 wait for the next sets.

### Closed 2026-11-10, batch 14 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2514 Python 3.10 breaks it | completed, CI tests 3.9-3.15 (`test_python.yml:17`), venv install | −troubleshooting, +question, +legacy motionEye |
| #2533 `output_pictures center` | completed, answered (MichaIng) | question, +motion, +legacy motionEye |
| #2489 frame rate / resolution dimmer | completed, answered, UI only (`main.js:1794`) | question, +legacy motionEye |
| #2506 PIR sensor on motionEyeOS | not planned, duplicate of #1138 | −question, +duplicate, +feature, +Raspberry Pi |
| #452 flip the image | not planned, `flip_axis` in Extra Motion Options | motion, feature, +legacy motionEye |

### Closed 2026-11-10, batch 14 second set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2438 DFRobot low light camera | completed, works with veye's V4L2 driver | −troubleshooting, +question, +Raspberry Pi, +legacy motionEye |
| #2417 mask adds false positives | not planned, no reply; privacy vs detection mask (zagrim) | troubleshooting, +motion, +legacy motionEye |
| #2448 webcam missing on Bullseye | not planned, went back to Buster (0.42.1) | troubleshooting, Raspberry Pi, +legacy motionEye |
| #2461 timelapse error | not planned, no answer; #2437 in 0.43.1, libcurl without RTSP | troubleshooting, +legacy motionEye |
| #1484 high CPU on a Pi 4 | completed, answered (Motion decoding) | −troubleshooting, +question, +motion, +Raspberry Pi, +legacy motionEye |

### Closed 2026-11-10, batch 14 third set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #1829 browser cannot play the movies (Docker) | completed, answered (quality 100%, passthrough) | −motionEyeOS, −troubleshooting, +question, +docker, +legacy motionEye |
| #2419 slow fps over dataplicity | not planned, bandwidth (MichaIng) | troubleshooting, +Raspberry Pi, +legacy motionEye |
| #2433 4K camera on a Pi 4 (HA add-on) | completed, answered (Motion decoding) | question, Home Assistant addon, +motion, +Raspberry Pi, +legacy motionEye |
| #2526 Volumio held broken packages | not planned, 2022 install script | troubleshooting, +Raspberry Pi, +legacy motionEye |
| #2530 D-Link as Network Camera garbled | not planned, no answer | troubleshooting, +motion, +Raspberry Pi, +legacy motionEye |

Kept #1630 (recording continues past the schedule, seen on 0.43.0), #1463 (Clean Cloud with a custom
period), #2525 (watch a movie while recording).

Closed 2026-11-10 (user OK):
- #2494 completed, record on the hub via a Network Camera with the Pi Zero's stream; #2486 (0.43.1)
  fixed stream auth; labels question, +Raspberry Pi, +legacy motionEye.
- #2453 not planned, 0.42.1 on the legacy camera stack; labels troubleshooting, +motion,
  +Raspberry Pi, +legacy motionEye.

Kept #2532 as a live bug (−troubleshooting, +bug): the frame page of a remote camera is rendered
without `static_path='../../../static/'` (`handlers/picture.py:328`, `:355`; local cameras pass it at
`:323`), so the global `static/` (`server.py:468`) makes `/picture/<id>/frame/static/...` 404, as in
the report's log. Fix not made yet; not reproduced on a device.

Batch 14 done: 17 closed, 8 kept.

### #2532 fix waiting for a Pi check (2026-11-10)

Branch `fix/remote-frame-static-path` on the fork (55b5eda9, on dev@upstream 71c81138), no PR yet:
both remote branches of `PictureHandler.frame()` now pass `static_path='../../../static/'`.
Tests: two new ones in `tests/test_handlers/test_remote_frame.py` fail without the fix (2 failed,
1 passed) and pass with it; full suite 527 passed (python:3.12-slim); ruff, codespell clean.

Pi check before the PR (user, on return): the Pi runs motionEye with its camera; a hub (second
motionEye, e.g. on the PC or in Docker) adds it as a Remote motionEye Camera. Open the hub's embed
URL `http://<hub>:8765/picture/<id>/frame/` with the browser's network tab: on dev the CSS/JS come
from `/picture/<id>/frame/static/...` and answer 404, with the branch from `/static/...` with 200,
and the picture shows. Also check a local camera's embed URL is unchanged.

## Batch 15 (open.json rows 350-374)

Kept for now: open feature requests (#2579, #1440, #2592, #2598, #2379); #2543, #2504, #2548, #2554,
#2549, #2559, #2568, #2581, #2164, #1435, #1895, #2603, #2605, #2609, #2607 wait for the next sets.

### Closed 2026-11-10, batch 15 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2546 RTSP not supported in QNAP Docker | not planned, old `ccrisan` image, ffmpeg lib error | question, docker, +legacy motionEye |
| #2558 Wi-Fi drops on motionEyeOS, Zero 2 W | not planned, motionEyeOS | question, +motionEyeOS, +Raspberry Pi, +legacy motionEye |
| #2565 motion_44 branch tools | not planned, #2462 merged in 2022 | CI/CD, +docker, +legacy motionEye |
| #2571 cannot change port 8765 | not planned, no answer (`port`, sample:33) | troubleshooting, +legacy motionEye |
| #2599 pillow build error, Zero W Docker | not planned, no answer | docker, troubleshooting, +Raspberry Pi, +legacy motionEye |

### Closed 2026-11-10, batch 15 second set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2548 USB cameras show nothing (0.42.1) | not planned, no reply to MichaIng | troubleshooting, Raspberry Pi, +legacy motionEye |
| #2549 fps drop when remote | not planned, 4G bandwidth | troubleshooting, +legacy motionEye |
| #1435 picture too bright at high resolution | not planned, legacy camera stack | troubleshooting, +motion, +Raspberry Pi, +legacy motionEye |
| #2607 dropped frames (0.42.1) | not planned, no follow-up | troubleshooting, +legacy motionEye |
| #2164 one camera falls behind over time | not planned, no reply | −question, troubleshooting, +legacy motionEye |

Open #2543 relabelled −troubleshooting, +bug: `on_event_start` commands run one after another
(`'; '.join`, `config.py:1545`) and `sendtelegram` sleeps the picture time span
(`sendtelegram.py:233`), so the web hook and command wait for it; still so on dev.

### Closed 2026-11-10, batch 15 third set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2554 iPad landscape gets one column | completed, fixed by #3502 (was `windowWidth <= 1200`), linked, milestone v0.45.0 | −troubleshooting, +enhancement |
| #2609 max password length | completed, argon2 hash since 0.44.0; 30/34/40/200-char passwords verified in Docker | question, +legacy motionEye |
| #2603 third camera stream closed (HA add-on) | not planned, old add-on | troubleshooting, Home Assistant addon, +legacy motionEye |
| #2605 two Pis share settings | not planned, no replies (cause assumed) | troubleshooting, +Raspberry Pi, +legacy motionEye |

Kept #2504 (default movie codec `h264_omx` when ffmpeg lists it, `config.py:2620`) and #2581 (no
picture while the network share is down).

Batch 15 done: 14 closed, 11 kept.

## Batch 16 (open.json rows 375-399)

### Closed 2026-11-10, batch 16 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2613 Docker build fails inside `docker/` | completed, build from repo root with `-f docker/Dockerfile .` (`docker/README.md:87-100`) | docker, documentation, +legacy motionEye |
| #2652 cannot write to the recording folder | completed, zagrim answered: motionEye runs as `motion`, give the group write access | question, +legacy motionEye |
| #2661 record the main stream, detect on the substream | completed, zagrim answered: `netcam_high_url` + Movie Passthrough | question, +motion, +legacy motionEye |
| #2665 finer frame change threshold | not planned, duplicate of #697 | enhancement, +duplicate |
| #2670 which Raspberry Pi / OS | completed, answered: 32/64-bit Raspberry Pi OS, Docker armv7/arm64 (`docker.yml:63`) | question, +Raspberry Pi, +legacy motionEye |

## Pi check 2026-11-10 evening (#2532, #1312)

Pi 5 (Camera Module 3, Motion 4.7.1), motionEye at 192.168.0.6:8765.

**#2532** (`fix/remote-frame-static-path`, 55b5eda9). Hub = python:3.12-slim container on the PC with
the Pi as a Remote motionEye Camera (`@remote_secret` = the Pi's `@client_secret`). Static files
named in the hub's `/picture/1/frame/`, resolved against that URL:

- dev 71c81138: all 11 (`manifest.json`, `static/css/*`, `static/js/*`, `static/img/*`) under
  `/picture/1/frame/...`, all 404.
- branch: all 11 under `/manifest.json`, `/static/...`, all 200. In the browser the branch page has
  jQuery and the three style sheets loaded (UI and login dialog drawn).
- After logging in to the test hubs, `/picture/1/current/` returned the Pi's 640x480 JPEG on both.
- Local camera unchanged: the Pi itself on the branch serves its own frame page's static files
  from `/static/...` with 200 (line 323 already did this).

Pi back on dev 71c81138 afterwards.

**#1312** (Bearer token for a netcam): works with Motion 4.7.1. A test MJPEG server on the Pi
answered 401 without `Authorization: Bearer s3cr3t`.

- Motion alone with `netcam_url http://127.0.0.1:9000/s` and
  `netcam_params headers=Authorization: Bearer s3cr3t`: the server got the header, the snapshot was
  saved; Motion logs "No trailing CRLF found in HTTP header. Adding it." (harmless).
- Through motionEye (camera added as a netcam, then `netcam_params` set as an Extra Motion Option,
  load/save round trip twice via `motion_camera_dict_to_ui`/`motion_camera_ui_to_dict`/`set_camera`):
  the option stays in Extra Motion Options, `camera-2.conf` gets
  `netcam_params headers=Authorization: Bearer s3cr3t,keepalive = off,tolerant_check = on`, the
  server got exactly `Bearer s3cr3t`, and Motion's webcontrol reports "Camera2 Connection OK".
  Test camera removed afterwards.

PR #3542 opened 2026-11-10 for #2532 (user OK after the Pi check): assignee, bug, Python,
milestone v0.45.0, closes #2532. Pi powered off afterwards (user).

Closed 2026-11-10 (user OK): #1312 completed, how-to with `netcam_params headers=...` under Extra
Motion Options (`http://` only; `https://` not tried); labels −feature, +question, +motion,
+legacy motionEye.

### Closed 2026-11-11, batch 16 second set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2616 UI frame rate vs substream FPS | completed, zagrim answered; Frame Rate is Motion's `framerate` (`config.py:1091`) | question, +motion, +legacy motionEye |
| #2622 Pi 3 one core at 100%, hardware encoding | completed, zagrim answered; H.264/V4L2M2M offered where available (`main.html:798`) | question, +motion, +Raspberry Pi, +legacy motionEye |
| #2624 dependency version constraints | not planned, open on purpose; CI installs latest on 3.9-3.15 (`test_python.yml:27`) | CI/CD, +legacy motionEye |
| #2606 CPU 300% with 3 cameras | not planned, no reply; software H.264 decoding (not measured), substream advice | troubleshooting, +motion, +docker, +Raspberry Pi, +legacy motionEye |
| #2629 ECONNREFUSED, HA add-on 0.18.0 | not planned, container stopping belongs to the add-on | troubleshooting, Home Assistant addon, +legacy motionEye |

Kept: #2614 (Matter) and #2618 (Pi status log), feature requests.

## PRs #3543 (#2504) and #3544 (#2543), 2026-11-11

**#3543** default movie codec `mp4`. Debian trixie ffmpeg 7.1.5 lists `h264_v4l2m2m` on x86_64 and on
the Pi 5; `motionctl.has_h264_v4l2m2m_support()` is True there, dev's default for a new camera is
`mp4:h264_v4l2m2m`, and the encoder fails ("Could not find a valid device"). Pi 5 event recording:
with it no movie (`ffmpeg_set_codec`, `event_ffmpeg_newfile` errors), with `mp4` 36 frames H.264.
The Pi's own camera-1.conf had `mp4:h264_v4l2m2m` from this default.

**#3544** senders last in `on_event_start`. Pi 5, Telegram 10 s, webhook to a local server, `touch`
command, `eventstart`: dev webhook 12.6 s / command 12.7 s after the trigger, branch 0.5 s / 0.6 s.
Background (`&`) rejected: `x &; y` is a syntax error with the `'; '` join; a self-detaching sender
would be a zombie under PID 1 meyectl in Docker (`server.py:239-241` reaps only multiprocessing).
Pitfalls in the test: Motion expands `%s`/`%N` in commands (so `date +%s.%N` logs the event time),
and `find_command` outside the server needs `sys.argv`/`settings.config_file` set.

Pi restored from `~/meye-backup-20261111`, dev bd5225b0 reinstalled.

### Closed 2026-11-11, batch 16 third set (user OK)

All not planned.

| Issue | Reason | Labels after |
|---|---|---|
| #1251 Xiaofang RTSP black | no logs from a current release; URL goes to Motion as `netcam_url` (`config.py:871`) | troubleshooting, +motion, +legacy motionEye |
| #2636 RTSP stops after months (0.42.1) | Python 2 release, no further reports | troubleshooting, +legacy motionEye |
| #2634 Pi 3 at 100% with RTSP | no reply to aaronouthier; software decoding (not measured) | question, +motion, +Raspberry Pi, +legacy motionEye |
| #2653 snap on KDE Neon | snap not ours; venv install listens on 0.0.0.0, lists `v4l2-ctl --list-devices` | troubleshooting, +legacy motionEye |
| #2563 CSI camera on Pi Zero 2 W | MichaIng answered legacy stack; libcamera tracked in #2425 | troubleshooting, Raspberry Pi, +duplicate, +legacy motionEye |

Left for later in batch 16: #2659 (wiki donation link, not checked yet), #2617, #2544, #2626, #2628, #2122, #2668, #2669.

### Closed 2026-11-11, batch 16 fourth set (user OK)

All not planned.

| Issue | Reason | Labels after |
|---|---|---|
| #2122 Reolink grey screen (add-on, 0.42.1) | mixed setups; one cause: Surveillance User named like the admin | troubleshooting, Home Assistant addon, +legacy motionEye |
| #2668 add-on 0.18.0, no feed | SMB mount errors; kernel default sec mode tried first now (`smbctl.py:244-259`) | troubleshooting, +Home Assistant addon, +legacy motionEye |
| #2669 strange rendering | screenshots only, no replies | troubleshooting, +legacy motionEye |
| #2626 refused to connect | no follow-up; `listen 0.0.0.0`, `port 8765` defaults | troubleshooting, +Raspberry Pi, +legacy motionEye |
| #2544 Annke I51DM RTSP | no reply to Pyanne's manual URL | troubleshooting, +motion, +Raspberry Pi, +legacy motionEye |

Kept: #2659 (the wiki Home.md still has Calin's PayPal donation link, lines 5-6; maintainers' call).
Left for a Motion check: #2617 (still JPEGs as a camera), #2628 (C615 zoom).

## Batch 17 (open.json rows 400-424)

### Closed 2026-11-11, batch 17 first set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2601 next release | completed, PyPI releases via #2675 (linked, milestone v0.43.1); 0.44.0 current, 0.45.0b1 pre-release | question |
| #2645 how to contribute | completed, MichaIng answered | question, +legacy motionEye |
| #2637 motion-triggered plus 24 h recording | completed, zagrim answered; ffmpeg or a second camera on the stream (clavay, not tried) | question, +motion, +legacy motionEye |
| #2689 Run a Command with discord_webhook | completed with the answer: commands run as `motion` (`motioneye.systemd:9`), use the venv's python | −troubleshooting, +question, +motion, +legacy motionEye |
| #2673 "Unable to open video device" (HA) | not planned, no replies | troubleshooting, +Home Assistant addon, +legacy motionEye |

To check: #2680 (USB stick missing from Storage Device), whether the disk listing drops exFAT.

## #2765 takeover survey (libcamerify), 2026-11-11/12

Why it is not merged (PR thread read in full): strips stopped in 2023-11 (Pi crashed, gave up); testers
then failed because Motion before 4.6.0 fails under libcamerify on arm64 (Motion#1644, fix b760d0be,
in 4.6.0+) and Motion before 4.7.0 leaves zombie shells under libcamerify (#2900, fix 629b3bab
"Remove signal handling from webu_start", in 4.7.0+). Debian: bookworm 4.5.1 (neither fix), trixie
4.7.0, Pi OS trixie 4.7.1. MichaIng's open point (2026-10-20): wrap motion only or the whole of
motionEye (so `v4l2-ctl` sees the shim). His 2024-01 idea: `motioneye_init` asks about a camera
module, installs `libcamera-tools` and sets the option. PR conflicts with dev now.

Pi 5 check (trixie, Camera Module 3 imx708, motion 4.7.1, libcamera 0.7.2+rpt, dev 0.45.0b1):

| | motion only wrapped (as #2765) | whole motionEye wrapped (wiki / drop-in) | not wrapped |
|---|---|---|---|
| camera 1 (`/dev/video0`, 640x480) | Connection OK, MJPEG stream | Connection OK, MJPEG stream | `VIDIOC_STREAMON: Invalid argument`, no picture |
| `/dev/video0` name in `v4l2ctl.list_devices()` | `rp1-cfe` | the camera's libcamera path | `rp1-cfe` |
| `/dev/video0` resolutions | 18 `COMMON_RESOLUTIONS` (v4l2-ctl says Stepwise, `v4l2ctl.py:121-126`) | 43 real sensor modes | 18 common |
| controls (`list_ctrls`) | 0 | 0 | - |
| devices in the add dialog | 29 | 29 (11 named after the camera) | 29 |
| zombies after 8 events, 127 pictures | 0 | 0 | - |

motion-only was simulated with `motion_binary` pointing to a script that execs `libcamerify motion`.
So: both wraps record; only the whole-motionEye wrap gives real resolutions and a camera name; neither
fixes the 29-node list or gives controls; #2900 does not reproduce on motion 4.7.1. Pi restored
from `~/meye-backup-2765` (drop-in wrap kept, as before).

### #2765 takeover implemented, 2026-11-12

Branch `feat/libcamerify` (fork, on dev 925dcc07, no PR yet; user chose the whole-motionEye wrap):
`libcamerify <path>` in motioneye.conf; `meyectl startserver` re-execs itself once under it
(`os.execv(libcamerify, [libcamerify, sys.executable, *argv])`, marker env `MOTIONEYE_LIBCAMERIFY`);
missing path logs an error and starts without it. Co-author Stian Indal Haugseth (strips).
Tests: 5 new in `tests/test_meyectl.py`; 555 passed, mypy, ruff clean on the Pi (Python 3.13).
Python 3.9 and Docker not run (Docker engine down).

Pi 5 (plain ExecStart, drop-in removed): server and motion both with `LD_PRELOAD=v4l2-compat.so`,
camera 1 Connection OK and MJPEG stream; motion killed with SIGKILL came back under libcamerify;
systemd MainPID is the re-exec'd server; a wrong path logs "libcamerify not found ..., starting
without it" and the service stays active (camera then "Lost connection"). Pi restored afterwards.

Also 2026-11-12: #3543 merged (925dcc07); its branch deleted locally and on the fork. Rebased
fix/senders-last (#3544), chore/ruff-bandit, repro/freebsd*; 551 / 550 passed on the Pi.

### #3544 review, 2026-11-12

MichaIng approved. Marijn0: a custom command before the senders could stop them; free-cup-holder-exe:
a command ending in `&`/`;` makes the whole line a syntax error, a trailing `# comment` comments the
senders out. Verified in `sh`. Fixed in c98ece9a (user chose option A): relay, webhook, email,
Telegram, command (command last as on dev). Pi 5: webhook 0.5 s, Telegram 11.4 s, command 12.4 s
after `eventstart`, same with `exit 0` in the command. Tests: changed ones fail on the previous order
(9); 551 passed on 3.9 (Docker) and 3.13 (Pi). Title/body updated, reply issuecomment-6800406017.
The command still waits for the time span, so #2543 is fixed for the webhook only.
feat/libcamerify: 3.9 in Docker 555 passed, mypy/ruff clean.

### Merges and #2765 takeover PR, 2026-11-12

Merged: #3538, #3540 (free-cup-holder-exe), #3545 (`9cfb176a`), #3544 (`e765d633`). Branches
`chore/ruff-bandit` and `fix/senders-last` deleted locally and on the fork; dev = `e765d633`.
#3545 CI: test_install failed once on a runner DNS error (`security.ubuntu.com`), green on rerun.
MichaIng's #3545 questions answered (issuecomment-6809272754): S402 is preview only, `shell=shell`
is S603 (ignored) in ruff vs B602 in bandit, `shell=True` calls still S604. #3539 rebased onto #3538
re-reviewed: only its own 2 files left, 564 passed; nothing posted (user).
Rebases: `fix/senders-last` conflicted with #3540 (Telegram `values`), resolved keeping #3540's
values and `senders.append`; `chore/ruff-return` conflicted with #3545 on `extend-select`, now
`["C901", "E501", "I", "UP", "S", "RET"]`; `feat/libcamerify` got S606 (`os.execv`, noqa) and S103
(test chmod 0o755 -> 0o700) from the new S rules. 3.9: libcamerify 568, ruff-return 563 passed.
**#3546 opened** (`feat/libcamerify` `6680de12`): Supersedes #2765, credit strips, Refs #2425 #2812;
labels feature, Python, Raspberry Pi, motion; milestone v0.45.0; assignee us.
**#3547 opened** (`chore/ruff-return` `b8403379`): RET rules, labels CI/CD, Python; milestone v0.45.0.
#2543 (closed by #3544): added `docker`, `motion` (had `bug`, v0.45.0).

### #3546 review (MichaIng, pullrequestreview-5866808711), 2026-11-12

- Inline (sample conf, "motion version shouldn't matter"): it does. GitHub compare: b760d0be (Motion#1644,
  "libcamerify fails on arm64") not in 4.5.1, in 4.6.0; 629b3bab (#2900 zombies) not in 4.6.0, in 4.7.0;
  bookworm ships 4.5.1. Reply drafted (disagrees), waiting for the user's OK
- linux_init prompt: done in `8b75b566` (user: in this PR). Pi detected via /proc/device-tree/model, asked
  only with a terminal, `--libcamerify`/`--no-libcamerify`; installs libcamera-tools + libcamera-v4l2 and
  sets the option. Trixie container: 7 cases OK, shellcheck -o all clean (0.10.0)
- Packages (Debian trixie 0.4.0-7 and RPi OS 0.8.0+rpt20261104 indexes): libcamera-tools has
  /usr/bin/libcamerify and Depends on libcamera-v4l2 (= same version) and Qt 6; 140 packages vs 17 for
  libcamera-v4l2 alone (trixie slim, simulated). libcamerify is a sh script that only sets LD_PRELOAD to
  v4l2-compat.so, so installing libcamera-v4l2 only would be possible (asked in the reply draft)
- Auto-enable on any Pi: not done; USB cameras under the shim not checked (module had 0 controls)
- SyslogIdentifier: not needed with the re-exec; systemd in a trixie container: re-exec keeps
  `meyectl[pid]`, wrapping ExecStart gives `libcamerify[pid]`

### Closed 2026-11-12, batch 17 second set (user OK)

Order rebuilt from a fresh fetch (313 open, by last human comment).

| Issue | Reason | Labels after |
|---|---|---|
| #2559 Pi 4, 6 IP cameras, high load | completed, Pete123123 and wpresident answered; substream advice | question, +motion, +Raspberry Pi, +legacy motionEye |
| #2677 no config after the Bullseye wiki install | completed, MichaIng pointed to the README; `motioneye_init` creates the config (`README.md:45`) | question, +Raspberry Pi, +legacy motionEye |
| #2685 RTSP URL with `/1/1/` | not planned, no reply on the version; path kept as is (`utils/http.py:19`, `handlers/config.py:166`), not tried on a camera | troubleshooting, +motion, +legacy motionEye |
| #2747 CPU 100% in Docker on ESXi | not planned, no reply to MichaIng | question, +docker, +motion, +legacy motionEye |
| #1824 Media format unsupported | completed: hub cache dir `/tmp/MotionEye` recreated since #3509 (linked, milestone v0.45.0); High 4:4:4 in Firefox not tried | bug, -question |

Next: #2568 (editable mask is a 32-cell grid, `utils/__init__.py:46`), #1895 (0% threshold gives Motion
`threshold 0`?), #1378 (two identical USB cameras), #2714 (vs #1630), #2715 kept (feature).

### Closed 2026-11-12, batch 17 third set (user OK)

| Issue | Reason | Labels after |
|---|---|---|
| #2751 port 80 does not start | completed, MichaIng's `AmbientCapabilities=CAP_NET_BIND_SERVICE` drop-in; service runs as `motion` | -troubleshooting, +question, +legacy motionEye |
| #2756 Dropbox key expires (motionEyeOS) | completed, MichaIng answered; fix #2396 in the Python 3 releases | question, motionEyeOS, +legacy motionEye |
| #2692 Outlook "SMTP AUTH extension not supported" | not planned, no follow-up; STARTTLS then login (`sendmail.py:76-79`); Outlook mailbox setting not checked | troubleshooting, +external bug, +legacy motionEye |
| #2750 grey frames, 4K H.265 | not planned, no report from a current release; decoding explanation not measured | troubleshooting, +motion, +legacy motionEye |
| #2568 mask changes after saving, file sizes | completed: editable mask is 32 cells across (`main.js:1223-1236`); Captured Before/After in frames | question, +motion, +docker, +legacy motionEye |

Held: #1895 fix candidate (slider `min="0"`, `main.html:871`, gives Motion `threshold 0`,
`config.py:1238`; Motion needs >= 1); #1378 (identical USB cameras share a `/dev/v4l/by-id` name,
`v4l2ctl.py:144`, not tried); #2707 after #3546 merges; #2753 (empty password, "Not a supported
network camera") to trace.

### Batch 17, fourth set (closed 2026-11-12)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #2759 | completed | −troubleshooting +bug +legacy motionEye | fixed by #3543 (new cameras get plain `mp4`); linked, milestone v0.45.0 |
| #2773 | not planned | −troubleshooting +question +legacy motionEye | action scripts run without a terminal (`handlers/action.py:95`), curses cannot start |
| #2782 | not planned | +docker +legacy motionEye | old `ccrisan/motioneye:master-amd64` image, no follow-up since 2023 |
| #2779 | completed | +legacy motionEye | answered by zagrim (CPU decoding, resolution, fps) |
| #2791 | completed | +legacy motionEye | answered by zagrim (ffmpeg / `netcam_params decoder=`) |

Held from this read:
- #2706: libcamera in a container, waits for #3546 like #2707.
- #2100: `netcam_keepalive=1` works for two users; motionEye enables keepalive only on an HTTP/1.1 answer (`utils/mjpeg.py:105`, `config.py:886`). Whether a motionEye stream still gets keepalive off needs a Pi check.
- #2754: composite USB adapter, last question from 2023-06 unanswered; reread.
- #2776: "dev has a workaround" for libmicrohttpd, but no such code found (`grep -rni microhttpd motioneye/`); check.
- #2794: Telegram topics, no `message_thread_id` in `sendtelegram.py`; kept as a feature request.

### Batch 17, fifth set (closed 2026-11-12)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #2809 | completed | −question +bug +legacy motionEye | fixed by #3380 (unwritable mounts listed as "[No write access]"); linked, milestone v0.45.0 |
| #2806 | completed | −troubleshooting +question +legacy motionEye | `/media/<user>` from udisks is closed to `motion` (not tried on a Pi) |
| #2797 | completed | +legacy motionEye | `smb_shares` needs root (`motioneye.conf.sample:80`), service runs as `motion`; mount with the OS + Custom Path |
| #2569 | completed | +legacy motionEye | web files are `motioneye/templates/` and `motioneye/static/` |
| #2825 | completed | +motion +legacy motionEye | `lastsnap.jpg` is Motion's; File Storage "Run a command" gets `%f` (`config.py:1666`) |

Held from this read:
- #2803: Home Assistant + Deepstack, likely outside motionEye; propose closing next time.
- #2804: Pi Zero W camera v2 on libcamera, waits for #3546 like #2706.
- #1544: "mjpg client timed out" in Docker, not checked on a current version.

- #2794 (2026-11-12): a commenter confirmed no `message_thread_id` in `sendtelegram.py` (checked on dev@upstream e765d633) and gave a text-only curl workaround; −question +feature, kept open with a short reply.

### Batch 17, sixth set (closed 2026-11-12)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #2803 | not planned | −troubleshooting +external bug +legacy motionEye | HA integration + Deepstack; pointed to Video Streaming → Useful URLs → Snapshot URL |
| #2817 | completed | +motionEyeOS +legacy motionEye | motionEye installs on Raspberry Pi OS per README; motionEyeOS is separate |
| #2582 | not planned | +motionEyeOS +legacy motionEye | Wi-Fi of the motionEyeOS image, tracked in motioneye-project/motioneyeos#3065 |
| #2860 | completed | +legacy motionEye | Dahua DVR: one network camera per channel, RTSP URL (format not tried on that model) |
| #2745 | not planned | +docker +legacy motionEye | old `ccrisan/motioneye:master-amd64` image, as #2782 |

Not closed from this read:
- #2818: Tasmota webhook, URL with `%20` (like #1916); check how the webhook URL is handled before deciding.
- #2824: Docker video devices, a feature request with MichaIng's script idea; kept.

### Batch 17, seventh set (closed 2026-11-12)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #627 | completed | +motion +legacy motionEye | threshold % is of `width × height` (`config.py:1238`), Motion counts after masking |
| #2814 | completed | +motionEyeOS +legacy motionEye | exposure is the driver's; V4L2 controls listed (`config.py:1867`) |
| #2907 | completed | (unchanged) | reporter: #2871 and the dev branch fixed it |
| #2868 | completed | +legacy motionEye | credentials in the fields, not in the URL |
| #2855 | not planned | +motion +legacy motionEye | passthrough artefacts from the stream, 0.42.1 / Motion 4.3.2 |

Not closed from this read:
- #2818: a bug. Motion's `mystrftime` reads digits after `%` as a width (`util.c:464`, Motion 4.7.0) and copies an unknown specifier with its `%` (`util.c:578`), so `power1%20on` becomes `power1%on`; motionEye passes the webhook URL without escaping `%` (`config.py:1536-1559`). Fix idea: `%XX` (two hex digits) → `%%XX`. Not run against Motion yet.
- #2911: fullscreen as the normal user, check the code.
- #2904: Docker on Buster, MichaIng's test pending.
- #2895: grey screen, no details; look again next time.

### Batch 17, eighth set (closed 2026-11-12)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #2923 | completed | (unchanged) | reporter solved it by updating to the beta |
| #2936 | completed | +motion | zagrim's noise level / Show Frame Changes advice helped |
| #2935 | completed | +docker | `motioneyeproject/motioneye`; image built for 6 platforms (`docker.yml:63`) |
| #2926 | not planned | +legacy motionEye | 401 with no username gives "authentication failed" (`utils/rtsp.py:141`) |
| #2895 | not planned | +legacy motionEye | grey frame, no details since 2023 |

Held from this read:
- #2917: Camera Module 3 on libcamera, waits for #3546.
- #2925: "backup makes motionEye unreachable", check the restore code.

### Batch 17, ninth set (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #2933 | completed | (unchanged) | motionEye pulls streams, it does not take pushed ones; adminy's tunnel advice |
| #2764 | not planned | +legacy motionEye | MichaIng asked for `journalctl -u motioneye`, no reply since 2023 |
| #2949 | completed | +motion | harakka's answer; detection is Motion's (Automatic Threshold Tuning / Noise Detection, Show Frame Changes) |
| #2956 | not planned | +external bug | system pyOpenSSL vs pip cryptography; motionEye imports no OpenSSL; README installs into a venv (#3496) |
| #2954 | not planned | +legacy motionEye | Python 2.7 paths (0.42.1 or older), no error in the log, no reply |

Held from this read:
- #2953: no details; `log_to_file false` by default since #3394 (0.45.0b1), not sure it is the same cause; propose next time.
- #2952: a bug. `meyectl.py:42` calls `locale.setlocale(locale.LC_ALL, '')` unguarded; `LANG=de_DE.UTF-8` without the locale generated gives `locale.Error: unsupported locale setting` (python:3.9-slim). Fix idea: catch `locale.Error`.
- #2955: the `video_params palette=8` advice is lost on save (#2635, fix/video-params-palette); close after that fix.
- #2942: two identical C270s, only one listed; maybe `/dev/v4l/by-id` names collide, needs two identical cameras.

### Batch 17, tenth set (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #2981 | completed | (unchanged) | one program per camera; motionEye has no composite output; MichaIng's rpicam-vid idea |
| #3027 | completed | +docker | mount the disk into the container (shaynethiessen) |
| #2880 | completed | (unchanged) | action buttons are executable `<action>_<camera id>` scripts in the conf dir (`config.py:51`, `:2218`) |
| #2997 | completed | +motion | Motion 4.6 `mmalcam_params` takes raspivid options (release-4.6.0 `conf.c:474`); no MMAL in 4.7.0 |
| #2984 | not planned | +external bug | HA Lovelace cards grey while motionEye shows the cameras; Useful URLs to check |

Held from this read:
- #3022: libcamera camera, MichaIng pointed to libcamerify; waits for #3546.
- #2986: movie playback error, no details; propose next time with #2953.

### Batch 17, eleventh set (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #3035 | completed | +motion | Maximum Movie Length → `movie_max_time` (`config.py:1157`), zagrim's answer |
| #3040 | completed | +motionEyeOS | no rsync upload (7 services in `uploadservices.py`); File storage → Run a command gets `%f` |
| #2901 | completed | (unchanged) | MichaIng and zagrim: reinstall and restart, no live reload |
| #2986 | not planned | (unchanged) | playback error in one browser, no details since 2024 |
| #2953 | not planned | (unchanged) | no answers; `log_to_file false` by default since #3394 (0.45.0b1) |

Held from this read:
- #3037: SFTP "SSL peer certificate or SSH remote key was not OK" (two reporters). The SFTP connection sets no host key option (`uploadservices.py:1199-1236`); maybe libcurl checks `motion`'s known_hosts. Worth a Docker repro.
- #2927: Pi camera brightness fixed at high resolutions; its German Useful URLs part was fixed by #3020 (0.43.1). Brightness likely the driver, not checked.
- #3046: libcamera camera, waits for #3546.
- Next: #3064 (WebRTC, motionEye streams MJPEG), #3045, #3050 (no details).

### Batch 17, twelfth set (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #1214 | completed | +legacy motionEye | ONVIF cameras via RTSP; "RTSP/UDP Camera" in the Add Camera dialog (`utils/rtsp.py:235`) |
| #3072 | completed | +docker | reporter fixed it with a full Debian base; image is `debian:trixie-slim` now; `h264_omx` is an OMX hardware encoder |
| #3074 | completed | +legacy motionEye | `import settings` is 0.42.1-era code from the old wiki steps; README installs into a venv |
| #2089 | not planned | +legacy motionEye | notification command gets no file; File storage → Run a command gets `%f` |
| #3086 | not planned | (unchanged) | 0.43.0, no details |

Held from this read:
- #2560: OV5647 auto exposure above 1280x720, like #2927; likely the driver, not checked.
- #1430: `v4l2_palette=8` workaround, lost on save (#2635); like #2955.
- #3088: no images on motion; maybe a 0 % threshold (#3548), look again after #3548.
- #3070 (HA addon fps), #3071 (`netcam_high_url` stops the stream): no comments, check the code.

### Batch 17, thirteenth set (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #3104 | completed | +motion | Motion docs: passthrough movies have no privacy mask; privacy mask applies before detection |
| #3120 | completed | +external bug | HA 2026.11.0 `media_source.py` proxies motionEye media (`MEDIA_PROXY_URL`), absent in 2026.10.0 |
| #3103 | completed | (unchanged) | zagrim: `?` before the URL parameters |
| #3090 | not planned | +external bug | whole machine hangs, kernel/hardware (zagrim, reporter) |
| #2291 | not planned | +legacy motionEye | motionEyeOS boot; last release 20200606, dev20201026 |

Held from this read:
- #3116: HQ camera on libcamera, waits for #3546.
- Next: #3096 (USB resolution stays 640x480), #3098 (mosquitto command), both without comments.

### Batch 17, fourteenth set (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #2476 | completed | +legacy motionEye | a separate `motion` service held the camera (two confirmations) |
| #2295 | not planned | +legacy motionEye | old `master-amd64` image; camera-specific RTSP URLs worked for others |
| #3165 | completed | (unchanged) | MichaIng: no media encryption; Run a command with `%f` as a way |
| #3175 | not planned | (unchanged) | HEVC playback is the browser's; "H.264 (.mp4)" (`main.html:785`), default for new cameras on dev (#3543) |
| #3161 | not planned | (unchanged) | Edge file dialog freeze, no answer to MichaIng |

Kept from this read:
- #2541: continuous recording forces still images to All Frames, a real bug (zagrim).
- #779: IPv6 `listen`, likely a sample config doc change after testing; PR candidate.
- #3128: Dropbox refresh 409, no comments, check the code.
- Next: #3137 (HA addon, second RTSP camera grey, no reply).

### Batch 17, fifteenth set (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #3223 | completed | +motion | `%f` only in File storage → Run a command (ToeKneeFan, MichaIng) |
| #3244 | completed | (unchanged) | Motion's docs for the options; ToeKneeFan's one-picture + Run a command setup |
| #3222 | not planned | (unchanged) | maybe password characters; percent-encoded since 0.44.0 (#3296), re-add the camera |
| #3163 | not planned | (unchanged) | Marijn's password guess, fixed by #3296 (0.44.0); no reply since Feb |
| #3137 | not planned | (unchanged) | HA addon second camera grey, no reply since June 2025 |

From here on the list reaches issues opened in 2025-2026; only those without updates for months are proposed.

Held from this read:
- #3217: Czech UI gives `internal server error` (HA addon 0.23.0), no comments; `cs` locale exists; try to reproduce, maybe a bug.
- Next: #3209 (hostname cameras, no reply to MichaIng since 2025-11), #2889 (iDrive e2 S3, no reply to MichaIng since 2026-02).

### Batch 17, sixteenth set (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #3015 | completed | +motion | Motion's notice for non-YUV420P frames (`netcam_rtsp_check_pixfmt`); HW frames come back as NV12 (cuda/drm set it, release-4.7.0 `netcam_rtsp.c:408,460`) |
| #2925 | completed | (unchanged) | backup/restore limited to motion.conf, camera-*.conf, mask_*.pgm since 0.44.0 (#3338); not linked, cause not confirmed |
| #3209 | not planned | (unchanged) | hostname cameras, no reply to MichaIng since 2025-11 |
| #2889 | not planned | (unchanged) | boto3 timeout, no reply to MichaIng since 2026-02 |
| #2754 | not planned | +legacy motionEye | composite USB converter on 0.43.0 dev (2023), unanswered since |

The sorted list is now done up to issues updated in 2026-10/11; those are not proposed.

Held:
- #2911: fullscreen as the normal user, no comments; check the code or the UI.
- #3183: OV5647 on libcamera, libcamerify worked for a commenter; waits for #3546.
- #2887: 3 s freeze at the start of movies, Marijn asked in 2026-04; still open.
- #3217: Czech UI internal server error; try to reproduce.

### Held issues revisited (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #2927 | not planned | +external bug | `bcm2835-camera.c` (rpi-6.6.y): above `max_video_width`/`height` (default 1280x720) the still capture port is used (lines 40-41, 1176-1182); German URLs fixed by #3020 |
| #2560 | not planned | +external bug | same driver limit; `duplicate` kept (MichaIng pointed to #2425) |
| #2904 | completed | +legacy motionEye | image runs as root unless `--user` since 0.45.0b1 (#3484, `docker/entrypoint.sh`); not linked, cause not confirmed |

Pi checks to do when the Pi is up (user boots it on request):
1. fix/video-params-palette (#2635) on Camera Module 3 via libcamerify: `video_params palette=...` in Extra Options survives a save, Motion keeps streaming; decides #2955, #1430.
2. #2100: the Pi's motionEye stream as an MJPEG network camera, keepalive set automatically?
3. #2706: libcamerify inside the Docker container on the Pi.

### Pi checks, 2026-11-13 (Pi 5, Camera Module 3, Raspberry Pi OS trixie, motion 4.7.1)

Backup `~/meye-backup-2635`; afterwards restored, motionEye back on dev `413b7ce4`, v4l2loopback unloaded, Docker left installed (no images/containers).

**#2635 (fix/video-params-palette `68883675`)**
- The Camera Module 3 through libcamerify exposes no V4L2 controls (`camera 1 control listing failed, controls not updated`), so motionEye never rebuilds `video_params` for it: `palette=17` survived a save even on dev. Not the case the bug needs.
- Used a v4l2loopback device (`/dev/video42`, controls keep_format / sustain_framerate / timeout) fed by ffmpeg testsrc, added as a V4L2 camera:

| | `video_params` before | after a save (framerate 3, timeout 5) |
|---|---|---|
| dev `413b7ce4` | `palette=17,ID10025216=0,ID10025217=0,ID10025218=0` | `ID10025216=0,ID10025217=0,ID10025218=0` (palette lost) |
| fix `68883675` | same | `palette=17,ID10025216=0,ID10025217=0,ID10025218=5`; Extra Options shows `video_params palette=17` |

- Extra Options → `video_params palette=15` on the fix: file `palette=15,...`; Motion (debug log): `v4l2_pixfmt_select: 設定パレットのインデックス15. (YUYV)寸法640x480は機能しません` then `選択したパレット YU12`; current picture 200 image/jpeg.

**#2100 (MJPEG network camera, keepalive)**
- Not reproduced: camera 1's Motion stream (`http://127.0.0.1:9081/`, HTTP/1.1) added as a network camera the way the dialog does; pictures came with `keepalive = off` and with `on` (1 `motion_init` first-image error each, at start only).
- `/config/list/` answers `keep_alive: True` for Motion 4.7.1's stream (HTTP/1.1). The Add Camera dialog keeps it in the option's `_extra_attrs` (`main.js:4073-4080`) and sends it with the add request (`main.js:4147-4151`), since 7f4ba007 (0.26, 2015); `add_camera` then writes it (`config.py:886`). The test script did not send it, so its `keepalive = off` was the script's doing, not a bug.

**#2706 (libcamera in the container)**
- Debian trixie's libcamera 0.4.0 in `debian:trixie-slim` with the devices: `cam -l` lists no camera.
- With archive.raspberrypi.com added (libcamera 0.8.0+rpt): `rpicam-hello --list-cameras` shows imx708; `libcamerify v4l2-ctl -D` gives `Driver name: libcamera`.
- `FROM ghcr.io/motioneye-project/motioneye:edge` + raspi.sources + keyring + `libcamera-tools libcamera-v4l2`, `ENTRYPOINT ["/usr/bin/libcamerify", "/entrypoint.sh"]`, run with all /dev/media*, /dev/video*, /dev/v4l-subdev*, /dev/dma_heap/* and /run/udev: V4L2 camera /dev/video0 added, pictures 200 image/jpeg (real image; 320 wide padded to 384, green stripe, the "width a multiple of 128" note).

- #2706 closed 2026-11-13 (completed, +Raspberry Pi +docker): comment with the Dockerfile (Raspberry Pi libcamera + libcamerify entrypoint), devices and the width-128 note, from the Pi check above.
- #2100 kept for now. Correction (2026-11-13): the dialog does send `keep_alive` (see the Pi check), so there is no fix to make. Likely the older Motion stream answered HTTP/1.0, so keepalive was detected off (not checked); with Motion 4.7.1 the stream is HTTP/1.1 and both keepalive off and on gave pictures. Candidate to close as not reproducible.
- #2100 closed 2026-11-13 (not planned, labels unchanged): not reproduced on dev + Motion 4.7.1 (Pi check above); workaround given as `keepalive = on` in `netcam_params` of camera-N.conf (kept on save, `config.py:199-205`, `:233-236`), not via Extra Options (not checked).
- #3217 closed 2026-11-13 (completed, −troubleshooting +bug, milestone v0.43.1): Docker, `@lang cs`: `/` gives 500 on 0.43.1b5 (traceback in gettext of `main.html:595`, Czech msgstr had `% m = minuta`), 200 on 0.43.1, 0.44.0 and dev `413b7ce4`; fixed by Weblate Czech commits 2025-12-09/10 (63fdf93a etc., first in 0.43.1). Add-on 0.23.0 pins 0.43.1b5, add-on 0.24.0 pins 0.44.0 (their Dockerfiles).

### Held issues, Docker/code checks (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #3037 | not planned | (unchanged) | `SFTP.test_access()` against OpenSSH in Docker passed on Debian 13 (apt pycurl, libcurl 8.14.1/libssh2 1.11.1), Debian 12 (libcurl 7.88.1/libssh2 1.10.0) and PyPI pycurl 7.49.0 (libcurl 8.23.0/libssh2), with and without known_hosts |
| #3071 | not planned | +motion | `netcam_high_url` not handled by motionEye (grep), passed as is; same URL twice, maybe one-connection camera (not checked) |
| #3070 | not planned | +motion | framerate written to Motion; add-on issue #505 closed stale |

Kept:
- #3128 (Dropbox): after a 401, credentials are refreshed and the retried request's 409 is logged, then "refreshing credentials failed" is logged although the refresh worked (`uploadservices.py:778-793`); the 409 is likely the upload itself. Bug candidate, needs a Dropbox account.
- #2911: needs a browser check with a camera as the normal user.
- #2776 closed 2026-11-13 (completed, −external bug +bug, milestone v0.43.1, linked #2432): same chunked-stream preview corruption as #2401/#2871; #2432 (fd59632c) requests Motion's stream with HTTP/1.0, first in 0.43.1b1, final 0.43.1.
- #1544 closed 2026-11-13 (not planned, +legacy motionEye): 0.42.1 / motionEyeOS 20200606 reports, MJPEG client changed since (#2432, #3266), not checked on current.
- #2942 closed 2026-11-13 (not planned): two identical C270s; by-id collision not checked (needs two cameras).

Remaining held: waiting for PRs (#2804, #2917, #3022, #3046, #3116, #3183, #3088, #2955, #1430); bugs to fix (#2952, #2541, #779, #3128); active (#2887); browser check (#2911).

### After the #3548 merge (closed 2026-11-13)

| Issue | Reason | Labels | Note |
|---|---|---|---|
| #3088 | not planned | (unchanged) | no motion pictures; threshold 0 % disables detection, fixed by #3548 on dev (not linked, cause not confirmed) |
| #3251 | completed | −feature +question +Home Assistant integration | HA integration has a "Motion detection" switch per camera (2026.11.0 `switch.py`); Motion webcontrol pause/start (Marijn) |

No unlabelled open issues. Left open: features (#3393, #3323, #3259, #3211, #3187, #3121), recent activity (#3438, #3288, #3179), waiting for #3546 (#3183, #3116).

#2911 check, 2026-11-13 (dev 20bba78f in Docker, MJPEG test camera; in-app browser 1024x768 and the user's Chrome 991x842): the full screen button gives the same layout as admin and as user (frame 988x743 in Chrome, image 978x734; motionEye's fullScreenMode true). Only difference: the configure button for admin. Browser fullscreen (document.fullscreenElement) was entered in neither browser for either user, so with automated clicks the real fullscreen part is not checked; main.js doFullScreenCamera has no admin branch.

## Open issue labelling (from 2026-11-13, 25 at a time, oldest number first)

Labels of the open issues are rechecked in batches of 25 (user, 2026-11-13). Read by 3 read-only agents, code evidence rechecked on dev `20bba78f`; low-confidence feature → enhancement proposals are left as `feature`.

### Labelling batch 1 (#37 .. #562, applied 2026-11-13, user OK)

| # | Change | Why |
|---|---|---|
| #37 | feature → enhancement, +motion | both capture modes exist, only one can be chosen (`config.py:1397-1412`) |
| #144 | feature → enhancement | working schedule exists with one range per day (`config.py:1454`) |
| #192 | feature → enhancement, +motion | per-camera detection pause/start exists (`action.py:72`, #3468); all-at-once and delay missing |
| #251 | feature → enhancement, +motion | detection toggle API (`action.py:72`), schedule keeps manual change (#3506) |
| #279 | feature → enhancement | zipped download exists for pictures (`picture.py:132`), not movies |
| #302 | feature → enhancement | age-based cleanup exists (`@preserve_*`) |
| #235 | +motion | `eventstart`/`snapshot` actions (#2691, `action.py:64`) |
| #319 | +motion | rotation is Motion's `rotate` |
| #203 | +Raspberry Pi | reporter on a Pi 2 |
| #258 | +motionEyeOS | reporter on motionEyeOS, DDNS belongs there |

No change: #40, #122, #142, #165, #179, #190, #232, #277, #287, #338, #413, #446, #455, #541, #562.
Close candidates for a later set: #235 (eventstart), #251 (detection toggle; no status API), #319 (reporter said implemented, 2017-10-03).

### Labelling batch 2 (#565 .. #869, applied 2026-11-13, user OK)

New rule (user, 2026-11-13): `legacy motionEye` also goes on open bug/troubleshooting/question reports from 0.42.1 or older (before 2023-12-24), not only on close. Not on feature/enhancement requests, nor on issues our PRs fix.

| # | Change | Why |
|---|---|---|
| #565, #675, #676, #697, #736, #738, #766, #814, #869 | +motion | Motion options (`mask_file`/`smart_mask_speed`, config inheritance, `stream_motion`, `threshold`, `emulate_motion`, text drawing, `picture_output best`, `%f`) |
| #704 | +security | current-password check for admin password changes |
| #715 | +security | login notification |
| #708 | +Raspberry Pi | reporter's setup |
| #833 | +Raspberry Pi, +legacy motionEye | reporter's setup, 2018 report |
| #779 | question → enhancement, +documentation | asks for IPv6 in the sample/defaults; MichaIng 2025-07-23: mainly docs |
| #790 | +legacy motionEye | 2018 bug |

No change: #679, #698, #742, #771, #773, #788, #789, #825, #850, #852.
Close candidates: #679 (likely fixed by #3485, `main.js:1105` rows = 1 in full screen; not checked in a browser; no legacy as our PR fixes it), #742 (same request as #302, no maintainer statement).
