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

### To close (proposed, not OKed)

| # | Reason | Add on close |
|---|---|---|
| #529 | completed: one-picture mode, PR #616 (`252fe4f2`, 0.37), link PR | legacy? no (implemented) |
| #592 | completed: same, PR #616, link PR | — |
| #445 | duplicate of #2379 (notify only on first event) | duplicate, legacy motionEye |
| #659 | duplicate of #1223 (URL to switch notifications) | duplicate, legacy motionEye |
| #273 | duplicate of #251 (toggle detection by script) | duplicate, legacy motionEye |
| #330 | Motion 4.0 fast playback, fixed in Motion (motion#431) | legacy motionEye |
| #567 | same cause as #330 | legacy motionEye |
| #419 | Python 2 Jinja2 byte-compile warnings, upgrade worked; Python ≥ 3.9 now | legacy motionEye |
| #516 | USB bandwidth with 3 cameras (Motion error, lower resolution fixed it) | legacy motionEye |
| #538 | Motion cannot do it (ccrisan 2017) | legacy motionEye |
| #576 | D-Link connection lost, no logs, no follow-up | legacy motionEye |
| #609 | movies do not play, Pi Zero W, no details | legacy motionEye |
| #642 | notifications never fire, no details | legacy motionEye |
| #640 | low fps on Pi Zero, Raspbian 8 | legacy motionEye |
| #443 | mask with rotation (follow-up of #437); rotation handled in `config.py:1271` | legacy motionEye |
| #479 | answered; remaining problem was the motionEyeOS image | legacy motionEye |
| #400 | answered: hardware encoding through ffmpeg | legacy motionEye |
| #610 | uploads happen per new file (`relay_event.py:105`) | legacy motionEye |
| #666 | USB camera in a VM, worked on a Pi | legacy motionEye |
| #195 | wait for a USB mount at boot: solved with systemd by the reporter | legacy motionEye |

Pi needed: none for closing (#609, #640 only to reproduce).
