# Close candidates, round 2: Raspberry Pi issues

- Surveyed: 2026-10-28 (base: `dev@upstream` = `5dc324ed`, wiki `faee8a6` 2026-10-27), 898 open issues
- Method (**verified**): titles matching Pi keywords (raspberry, rpi, pi zero, libcamera, mmal, csi, bookworm, ...) → 103 issues;
  read body + last comments of 36 of them with `gh issue view`; checked the code on `dev` and the wiki
- Precedent (**verified**, timeline of the closed issues): maintainers close Pi camera issues as duplicates of
  #2683 / #2812 or point to the wiki `Troubleshooting#libcamera-camera-stack` (libcamerify) section:
  #2938, #3278, #2810 (MichaIng), #3295 (duplicate), #3081, #2948 (Marijn0), #2788 (MichaIng: MMAL removed since Bookworm)
- Not closing now (user, 2026-10-28): prepared in advance, close one by one with the user's OK

## A. Resolved or obsolete, no repro needed

| # | Title | Why (evidence) | Status |
|---|---|---|---|
| [#405](https://github.com/motioneye-project/motioneye/issues/405) | MMAL Support in motioneye | Implemented: `controls/mmalctl.py`, `mmalcam_name` in `config.py:98,860`, "Local MMAL camera" in the UI (grep on `dev`) | **closed 2026-10-29** ([comment](https://github.com/motioneye-project/motioneye/issues/405#issuecomment-6480391718)) |
| [#2778](https://github.com/motioneye-project/motioneye/issues/2778) | Python3 is required to install on Debian 12 bookworm | motionEye is Python 3 since 0.43: `pyproject.toml` `requires-python = ">=3.9"`; MichaIng pointed to it in 2023 | **closed 2026-10-29** ([comment](https://github.com/motioneye-project/motioneye/issues/2778#issuecomment-6480437426)) |
| [#2792](https://github.com/motioneye-project/motioneye/issues/2792) | Missing packages on lite bullseye armhf (wiki instructions) | Refers to wiki `Install-on-Raspbian-Bullseye`, deleted 2025-12-16 (same as the round-1 wiki closes) | **closed 2026-10-30** ([comment](https://github.com/motioneye-project/motioneye/issues/2792#issuecomment-6494467673)), `documentation` |
| [#2934](https://github.com/motioneye-project/motioneye/issues/2934) | MotionEye with Libcamera on Pi 4B and Debian 10/11 | Reporter runs jmichault's fork `motioneye.eo` (zagrim, 2024-03-12), not this project | **closed 2026-10-30** ([comment](https://github.com/motioneye-project/motioneye/issues/2934#issuecomment-6494558731)), `question` |
| [#2062](https://github.com/motioneye-project/motioneye/issues/2062) | Pi cam strange color pink | Reporter solved it with `awb_auto_is_greyworld=1` (NoIR camera); another user confirmed and suggested closing (2021-08-11). The wiki has a NoIR section now | **closed 2026-10-30** ([comment](https://github.com/motioneye-project/motioneye/issues/2062#issuecomment-6494596958)), `question` |
| [#2083](https://github.com/motioneye-project/motioneye/issues/2083) | Missing options in Camera Type menu | Reporter solved it (Pillow missing, old Python 2 install, 2021-04-01) | **closed 2026-10-30** ([comment](https://github.com/motioneye-project/motioneye/issues/2083#issuecomment-6503395682)), `question` already set |
| [#1496](https://github.com/motioneye-project/motioneye/issues/1496) | No image nor video raspi 0 w | Reporter: "The i2c was the problem" (2019-10-16) | **closed 2026-10-30** ([comment](https://github.com/motioneye-project/motioneye/issues/1496#issuecomment-6503398436)), `question` added |
| [#1408](https://github.com/motioneye-project/motioneye/issues/1408) | MotionEye does not work with RasPi Cam | Chrome streaming breakage #1401; a second reporter confirmed, the author did not answer (weaker) | candidate |
| [#406](https://github.com/motioneye-project/motioneye/issues/406) | Cant see csi local camera | 2017, legacy stack (`bcm2835_v4l2`, `gpu_mem`); hardware question, answered by ccrisan | candidate (weak) |
| [#2243](https://github.com/motioneye-project/motioneye/issues/2243) | IMPORTANT INFO: Bullseye CSI Camera Support | Informational note about the Bullseye legacy stack; legacy stack removed since Bookworm → duplicate of #2683 / #2812 | candidate |

## B. libcamera duplicates — check the wiki steps on the real Pi first

Point to the wiki libcamerify steps and #2683 / #2812, as the maintainers do. With the Pi and camera at hand,
first run the wiki `Troubleshooting#libcamera-camera-stack` steps on current Raspberry Pi OS so the pointer is
known to work (**not verified yet**).

| # | Title | Notes | Status |
|---|---|---|---|
| [#2684](https://github.com/motioneye-project/motioneye/issues/2684) | working on a libcamera workaround | zagrim pointed to #2425 / #2683 (2023) | candidate |
| [#2706](https://github.com/motioneye-project/motioneye/issues/2706) | Pi camera v2 in motioneye container no image | libcamera in Docker; libcamerify inside the container is not in the wiki → check on the Pi, or leave | needs check |
| [#2763](https://github.com/motioneye-project/motioneye/issues/2763) | Pi Zero W and Camera Module 3 | strips/MichaIng pointed to #2683 / #2425 | candidate |
| [#2798](https://github.com/motioneye-project/motioneye/issues/2798) | MMAL camera: "An error occured" (Camera Module 3) | Module 3 is libcamera only; MMAL removed since Bookworm | candidate |
| [#2799](https://github.com/motioneye-project/motioneye/issues/2799) | MotionEye mit RPi Camera Modul3 | zagrim pointed to #2425 / #2683 | candidate |
| [#3046](https://github.com/motioneye-project/motioneye/issues/3046) | Add camera does not find the pi camera | Reporter got it working via #2683; a remaining "nothing written" problem was not followed up | candidate |
| [#3056](https://github.com/motioneye-project/motioneye/issues/3056) | libcamera works, but no video from unicam | Marijn0 pointed to the #2812 steps (2024-09-30) | candidate |
| [#3255](https://github.com/motioneye-project/motioneye/issues/3255) | Unable to run on Pi Zero 2W (Camera 3 NoIR) | Fixed by the libcamera 0.7 packages (frepkovsky, MichaIng 2026-02-07) | candidate |

## C. Install on Pi — check with the README on the real Pi

| # | Title | Notes | Status |
|---|---|---|---|
| [#2906](https://github.com/motioneye-project/motioneye/issues/2906) | Install on Raspi 5 | Old wiki instructions; install with the README on a Pi 5 and close if it works | needs check |
| [#2957](https://github.com/motioneye-project/motioneye/issues/2957) | Install on Raspbian 12? | Wiki Bullseye page (deleted) + Tornado issue; README install on current Pi OS | needs check |

## Leave open (for now)

| # | Why |
|---|---|
| #3183 | MichaIng 2025-12: waiting for motion v5 libcamera and a way to list a single node; active |
| #3288, #3320 | Discussion in October 2026; #3320 labelled `external bug` |
| #3344 | Pi 5 has no H.264 hardware decoder (MichaIng); discussion until 2026-10-15 — ask before closing |
| #3116 | HQ camera resolution padding, a separate problem; needs a repro with an HQ camera |
| #2425, #2683, #2812, #2900 | Tracking issues (milestone) / libcamerify zombie bug |
| #2453, #2927 | Auto exposure at high resolutions; could be checked on the Pi later |

## Real Pi check (2026-10-28)

Setup (**verified** over SSH): Raspberry Pi 5 Model B 4 GB, Raspberry Pi OS (Debian 13 trixie, 64-bit, desktop image),
kernel `6.12.47+rpt-rpi-2712`, Camera Module 3 (`imx708`), libcamera 0.7.2, rpicam-apps 1.14.0.

| Step | Result |
|---|---|
| `rpicam-hello --list-cameras`, `rpicam-still` | imx708 listed, still captured |
| README install (as written) | motionEye 0.44.0 + motion 4.7.1 installed, service `active`, HTTP 200 on :8765. **But step 2 fails**: `sudo python3 get-pip.py` → `error: externally-managed-environment` (exit 1), because the README sets `break-system-packages` only after it. It only worked because the desktop image ships `python3-pip`. Lite image not checked. `enh/venv` (#3066) removes get-pip, so it fixes this |
| Wiki libcamerify steps | `ExecStart=/usr/bin/libcamerify /usr/local/bin/meyectl ...`, service `active`; the camera is listed as `/dev/video0` (plus ~28 other `/dev/video*`/`media*` nodes in the add dialog) |
| Add as Local V4L2 camera | Picture shown, but at the **default 320x240 the right part is a green band**: motion `v4l2_pixfmt_adj: 320x240 → 384x240` (stride 384). At **640x480** the frame is complete, no stride warning. Width test: 640, 1280, 1920 kept; 320→384, 800→896, 960→1024, 1600→1664 — the width must be a **multiple of 128** (960 and 1600 are multiples of 64 and still padded). Same symptom as #3116 (resolution padding) |
| Side notes | Applying the resolution in the UI was refused ("Make sure all configuration options are valid!") with empty admin/user passwords marked invalid (cause **guessed**, not checked); set via `camera-1.conf` instead. Login was lost after `systemctl restart motioneye` |

Consequences for the candidates:
- B (libcamera duplicates): the wiki steps work on Pi 5 + Camera Module 3 + trixie, **with a resolution whose width is a multiple of 128** — worth adding to the wiki before pointing users to it
- #3116: no longer "needs an HQ camera" — the padding problem reproduces with Camera Module 3 on Pi 5; candidate for a fix (default/allowed resolutions) rather than a close
- C (#2906, #2957): install on Pi 5 trixie works, except the get-pip step; close after `enh/venv` is merged, or now with a note
