# Pre-research of the open issues (2026-11-15)

The user, 2026-11-15: implementation pauses here because the held branches are enough stock, and rebasing more would cost effort. Meanwhile every open issue is researched, so that (a) the next implementation round can start at once and (b) reporters can be asked now.

**Method**
- 144 open issues; 125 researched.
- Left out:
  - held branches or open PRs: #2135, #2541, #1630, #766, #2411, #771, #3393, #1290, #3128, #779, #1887, #2214, #972;
  - waiting for an answer: #1958, #2887, #2710, #2866, #3096, #3320.
- Six read-only agents each read about 21 issues in full, with all comments, against `upstream/dev` 1e039f66.
- Each issue went into one category:
  - READY: implement now;
  - ASK: question for the reporter;
  - CLOSE?: close candidate;
  - DECIDE: needs a maintainer decision;
  - LARGE: big, or belongs to motion.
- Evidence tags: **V** = read in code, **D** = documented, **I** = inferred. No tests were run in this pass.
- The main claims were spot-checked by me on 1e039f66 (V):
  - `BaseHandler.head` only calls `finish()` (`handlers/base.py:301`), and `PictureHandler` has no `head`.
  - `webhook.py:56-74` has POST/POSTf/POSTj/GET only.
  - No `robots` anywhere.
  - The Dockerfile apt line has no mosquitto-clients.
  - The SMB opts have no `mfsymlinks` (`smbctl.py:245-276`).
  - `capture_mode == 'manual'` doesn't touch `@manual_snapshots` (`config.py:1487`).
  - The palette tests from #3551 exist (`tests/test_config.py:431-511`).
  - `monitor_<id>` (`config.py:2350`).
  - `_MAX_TASKS = 100` (`tasks.py:30,60`).
  - The Zipped button is pictures-only (`main.js:4602`).

## READY: can be implemented in the next round

| # | What | Size | Verify with | Note |
|---|---|---|---|---|
| #165 | `PictureHandler.head` delegating to `get` for current/download/preview, so HEAD gets auth, 404 and `image/jpeg` | S | handler tests (`fetch(..., method='HEAD')`) | no Pi |
| #852 | Webhook PUT/PUTf/PUTj next to the POST variants; 3 selects in main.html | S | `tests/test_webhook.py` | openHAB wants a plain-text body: consider PUT with the raw query as body (I) |
| #926 | "Invert mask" button (`toggleClass('on')` + `_matrixToMaskLines()`) for motion and privacy masks | S | Docker + browser, screenshots | no JS tests |
| #1244 | `/robots.txt` handler (`Disallow: /`, no auth), optional `X-Robots-Tag: noindex` | S | `tests/test_handlers/test_base.py` | |
| #1358 | "Remote motionEye UI" link for proto motioneye cameras (`device_url` minus `/config/N`) | S | two Docker motionEyes | |
| #1359 | Manual capture mode implies manual snapshots: `depends="captureMode!=manual"` on the switch, force `@manual_snapshots` on save | S | `tests/test_config.py` | near the #2541 branch's capture-mode code: do after it |
| #1949 | `mfsymlinks` in the SMB mount options | S | new `tests/test_smbctl.py` (mock subprocess) | live mount needs Samba + Pi |
| #676 | Browser preview throttled to 1 fps while `stream_motion` is on and no motion | S | Docker, DevTools request rate | |
| #877 | `mosquitto-clients` in the Docker image, or a README recipe for adding packages | S | docker build | kleini agreed in 2018; same Dockerfile line as `enh/no-fdisk-in-container` |
| #2824 | docker/README "Camera devices": `--device` one-liner and `--device-cgroup-rule='c 81:* rmw'` | S | docs | |
| #2794 | Telegram `message_thread_id` (forum topics): optional `@telegram_notifications_thread_id` | S–M | mocked tests; real check needs a bot + forum group | |
| #40 | Media browser renders in batches + IntersectionObserver (86k files freeze it today, `main.js:4461-4540`, `:4788-4808`) | M | Docker with ~50k dummy jpgs | |
| #232 | Multi-select delete in the media browser (#1020 is the same ask) | M | Docker + browser | after #40 |
| #1322 | Apply button only when something really changed (baseline JSON per config) | M | Playwright | |
| #2775 | Concatenated translatable strings → one `%(x)s` string with `.format()` (about 12 JS sites) | M | — | Weblate rule: English source strings only; those translations are lost until re-translated |
| #2914 | RTSPS: dispatch `rtsps` in `handlers/config.py:524`, TLS in `test_rtsp_url`, default port 322 | M | Docker with mediamtx (self-signed) | |
| #3259 | Send the movie to Telegram on `movie_end` (`sendVideo`, skip over 50 MB) | M | Telegram bot + Docker | MichaIng welcomed it with limits |

Suggested order: the S items with no overlap first (#165, #852, #1244, #926, #1358, #1949, #676), then #1359 after #2541 and #877 after the no-fdisk branch.

## ASK: questions to post now (answer what they are stuck on, then wait)

| # | Draft question (to be reviewed one by one before posting) |
|---|---|
| #2826 | The Embed URL `/picture/<id>/frame/` already scales to its window (`frame.js:64-70`). Logging in without input comes with API keys (#3524); once merged, could you try `http://user:<key>@host/...`? |
| #2857 | Cropping in motion can't change what the camera's own auto white balance sees. Which camera is it? For V4L2 cameras the camera controls under Video Device can switch off auto white balance. |
| #2955 | Please post `v4l2-ctl --list-formats-ext` and the motion log. `video_params palette=8` (MJPEG) in Extra Motion Options is kept on save from the next release (#3551). |
| #2969 | The RTSP password part is fixed by #3445. The USB message usually means a non-capture node: please post `v4l2-ctl --list-devices` and try the other `/dev/video*` or its by-id entry. |
| #2372 | Does it still happen on 0.44 with motion 4.5+? If so, what is the Doorbird's keyframe interval? With passthrough a movie can only start at a keyframe. |
| #2753 | Please post the headers of `curl -sv -o /dev/null -u admin: http://<camera>/snapshot.jpg` (and `/livestream/12`). The message means the camera answers OK but not with JPEG/MJPEG (`utils/mjpeg.py:94-130`). |
| #1902 | Encoding happens inside motion, not in a separate ffmpeg. Does Movie Format "H.264/V4L2M2M" (hardware) keep the Pi 4's load low enough? |
| #2033 | Please post the `gdrive:` lines of motioneye.log around a failed upload (timeout, memory or Google error). Drive uploads are one non-resumable request today (`uploadservices.py:376`). |
| #2077 | The `:8081` request comes from a "Simple MJPEG camera", which the browser loads directly. Add it as a network camera, or give it a proxied URL. Is that your setup? |
| #1463 | What is the exact Upload Location? Clean Cloud compares the first path part with the local folders (`uploadservices.py:1575-1580`), so a nested location may delete everything (I). Still on 0.43+? |

Already asked, waiting: #2861 (HA 2026.11 retest, asked 2026-11-07; stale close mid-December) and #3438 (browser checks, asked 2026-10-15).

Possible follow-up from #2969: list only V4L2 nodes with "Video Capture" in Device Caps (S, mocked `v4l2-ctl --info`).

## CLOSE?: close candidates (each with its own comment, about five a day, user OK each)

| # | Reason | Milestone / link |
|---|---|---|
| #3179 | `palette=8` now kept by #3551 | v0.45.0, link #3551. Marijn0 commented 2026-10-31: check the recent-comment rule first |
| #1430 | same, Extra Option `v4l2_palette 8` kept | v0.45.0, link #3551 |
| #190 | detection button with state icon on each frame since #3468 (`main.html:986`) | v0.45.0, link #3468 |
| #1846 | already possible with `monitor_<id>` (stdout over the frame, stderr = interval) | none |
| #2618 | same mechanism, e.g. `vcgencmd measure_temp; vcgencmd get_throttled` | none |
| #2921 | after #3524 merges (API key as Bearer or basic-auth password); decline query-string keys | link #3524 then |
| #1227 | http:// netcams no longer hit the size check since motion 4.4 (ffmpeg path rounds to 8); mjpeg:// still does | none; an optional check is M |
| #1378, #1451 | legacy motion 4.0 / bcm2835 stack, reporters gone | none, legacy label already |
| #2387, #2130, #1355 | belong to motion (no audio; overlay drawn by motion; frame counts) | none |
| #2210, #446, #179 | workaround with Run A Command (`zbarimg %f`, `mosquitto_pub`, ImageMagick crop); built-in support would need non-stdlib deps | none |
| #2614, #2115, #1129, #1254 | out of scope (Matter; rotating stream port; Google Home via HA; motion TLS breaks mjpgclient) | none |
| #2057 | UI passwords are argon2, configs 0600; camera/SMB/SMTP secrets must stay readable for motion and mount | none |
| #738 | answer with the webcontrol workaround, noting `webcontrol_parms 2` is needed since #3474 | none |

## DECIDE: questions for the maintainers

Grouped by area. Each needs one decision before code.

- **Working schedule** (after the overnight and #1630 branches):
  - #144: format for several ranges per day.
  - #142: notify when the schedule starts or ends.
  - #883: schedule interval snapshots.
  - #1315: notify only during the schedule.
  - #698: daylight schedule (lat/long, stdlib sunrise).
- **Capture modes** (after #2541):
  - #37: interval and motion stills together, as a switch or a mode.
  - #3093: snapshots every N ms during an event.
  - #736: comment once #2541 lands; motion-triggered stills with continuous recording is a motion limit.
- **Media browser**:
  - #279 / #3323: zipped movies only if streamed from disk.
  - #562: hover video preview.
  - #1527: mosaic thumbnail.
  - #814: best picture as the movie thumbnail.
  - #2766: thumbnail offset; our PR #3384 was closed, so shape and default are needed.
  - #2879: no `.thumb` files at all, or thumbs in a cache dir.
  - #1987: resizable group column.
  - #2114: timelapse over a date range; the backend mostly exists.
  - #2731: per-user preference toggle (MichaIng's idea), or close.
- **Notifications**:
  - #2379: mute window semantics.
  - #2166: keep settings while disabled, plus an on/off action.
  - #3001: Telegram at event end.
  - #2400: `on_camera_lost`/`on_camera_found` fields; the Extra Motion Options workaround can be posted now.
  - #2241: a separate picture command.
  - #715: `login_hook`.
  - #1924: `/health` (auth, which checks).
- **Uploads**:
  - #708 + #833: retry and the 100-task cap (`tasks.py:30`).
  - #413: overwrite switch.
  - #1007: SFTP key (path or stored; credit TheFlatEric).
  - #1339: FTP test writes a file.
  - #1375: rsync via Run A Command.
  - #2378: shared drives (needs Workspace).
- **Security / auth**:
  - #704: repeat field, or a current-password check.
  - #2473: trusted proxy header; after #3524.
  - #3211: action buttons admin-only.
  - #2205: normal user never reboots, then close.
- **Detection / UI**:
  - #192: all-cameras toggle.
  - #2172: persist pause.
  - #565: smart + editable mask.
  - #697: 2 decimals for the threshold.
  - #1441: pixel hint next to the %.
  - #455: cycle cameras.
  - #2169: chime.
  - #1273: system font fallback.
  - #1276: description.
  - #1158: latest-movie link.
  - #884: PNG touch icons, probably the real fix for iOS.
  - #788: brightness value.
  - #1107: frame-only listener or a proxy recipe.
- **Other**:
  - #773: expose motion's `timelapse_*`.
  - #880: high-res URL field (`netcam_high_url`).
  - #1816: sub-day retention.
  - #2442: log level in the GUI.
  - #2441: chunked MJPEG (HTTP/1.0 still works).
  - #2129: MotionPlus stance.
  - #2659: wiki donation link.
  - #2976: media-only camera.
  - #2854: encrypted zip (non-stdlib; likely decline).
  - #1338: AUR note in the README.

## LARGE: keep as features

#541 (multi-user), #675 (global defaults), #850 (camera groups), #1054 (activity log), #1058 (counts in the banner), #1287 (time-range browser), #1466 (motion per camera), #1850 (Drive link in the email), #1966 (watch while recording), #2157 (synced playback), #2598 (calibration library), #2631 (RTSP restreaming), #3063 (ONVIF; the eventstart/eventend actions are a workaround).

#3299 is MichaIng's meta topic; nothing for us.

## Questions posted

2026-11-15, first five (user OK; drafts re-read against the issues, unverifiable claims dropped): #2826 (Embed URL scales; can Wallpaper Engine send a #3524 key? iframe credentials in the URL may be blocked, not claimed), #2857 (V4L2 white balance control), #2955 (palette=8 kept from #3551), #2969 (non-capture node; #2972 is a different problem), #2372 (current add-on; keyframe interval, stated as "may"). Waiting; stale close if silent. Next five: #2753, #1902, #2033, #2077, #1463.

2026-11-15, second set (user OK): #2753 (curl headers with and without `-A "JUAN ProductCheck"`; exact Content-Type match in `utils/mjpeg.py`), #1902 (encoding is inside motion; H.264/V4L2M2M since 0.44.0, `main.html:883` on the tag), #2033 ("failed to upload file" + traceback, `uploadservices.py:1438-1442`), #2077 (Simple MJPEG camera is loaded by the browser directly, `main.js:5630-5632`).

#1463 reproduced before posting (user asked to check first): a test against dev 1e039f66 in python:3.9-slim (scratchpad `r1463/tests/test_r1463.py`; only `GoogleDrive._request` faked as a folder tree; the real `uploadservices.clean_cloud` and `GoogleDrive.clean_cloud` run):
- Upload Location `/motioneye`, Drive `2026-11-10`, `2026-11-14`, local `2026-11-14` → Drive keeps `motioneye/2026-11-14`. Correct.
- Upload Location `/motioneye/Camera1`, same days → Drive keeps only `motioneye`: `Camera1` with every day, today's included, is deleted. **Bug**: `clean_cloud` takes only the first part of the location (`next(p.strip() for p in cloud_dir_user.split('/') ...)`) and compares its children with the local day folders.
- Two cameras sharing `/motioneye`: camera 1's cleanup deletes `2026-11-12`, which camera 2 may still keep locally. A second, smaller problem (inferred that a user would share a location; observed that it deletes).
→ #1463 moves to READY: resolve the whole Upload Location (`_get_folder_id_by_path`, without creating it), then compare its children. The repro test becomes the regression test. Docker only.

2026-11-15: #1463 fixed instead of commented (user: just the PR, Fixes is enough) → **submitted as [#3559](https://github.com/motioneye-project/motioneye/pull/3559)** (`fix/clean-cloud-location`, e2e9c982 on dev 1e039f66). `uploadservices.clean_cloud` keeps the whole location (parts joined, empty = root → skipped instead of StopIteration); `GoogleDrive.clean_cloud` walks it with `_get_folder_id_by_name(..., False)`. 3 tests in `tests/test_uploadservices_google.py` (`_DriveFolders` fake answering `_request`); 2 fail on dev. 3.9: ruff, format, mypy clean, 612 passed, shellcheck ok. Not tried against a real Drive. PR: bug, Python, v0.45.0, assignee. #1463 relabelled −troubleshooting −legacy motionEye +bug.

## Closed from this research

2026-11-15 (user OK): #1430 (completed; v0.45.0, #3551 linked; own comment then edited in place: `v4l2_palette 8` "is kept, shown as `video_params palette=8`", per `test_an_option_of_motion_43_shows_as_it_is_saved`), #1846 and #2618 (completed, no milestone: `monitor_<id>`, `config.py:2350-2357`, `monitor.py:57-60`, cache cleared on each config GET `handlers/config.py:74`), #2387 (not planned: motion has no audio), #2130 (not planned: no ms specifier in motion 4.7.1 `util.c`; `%q` = frame within the second; `webcontrol_parms 0` since #3474). #3179 (completed; v0.45.0, #3551 linked; user OK'd it as its cause is clear: MJPEG/H.264 only above 640x480, YUYV chosen). Not closed: #190 (kept on 2026-11-09: no overlay in recordings).

2026-11-15, second set (user OK, closed the same day although over the ~5/day pace, at the user's choice): #1355 (motion counts frames; jasaw asked for a motion request), #2614 (Matter out of scope), #2115 (browser kiosk; UI cycling is #455), #2210 (Run A Command on picture save with `%f`, e.g. `zbarimg`), #2057 (argon2 + 0600 since 0.44.0; motion/mount need clear text). All not planned, no milestone, labels unchanged. Not closed, cause unclear: #1378 (identical USB cameras; maybe a shared persistent name, inferred), #1451 (Pi 4 frame rate; needs a Pi check). Left: #1227, #446, #179, #1129, #1254, #738, #2921 (after #3524), #190 (kept).
