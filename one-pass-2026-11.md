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

### To close next (proposed, not OKed yet)

| # | Reason | Labels to add |
|---|---|---|
| #385 | pink picture, likely hardware | external bug, Raspberry Pi, legacy motionEye |
| #335 | two identical USB cams, no replies | Raspberry Pi, legacy motionEye |
| #228 | brightness slider steps of 5; sliders now snapMode 0, `main.js:1009` | legacy motionEye |
| #439 | stream reconnect: UI re-polls at 1 fps on error, `main.js:5660` (not for simple MJPEG, `main.js:5641`) | motion |
| #315 | ship ffplay: out of scope | Raspberry Pi, legacy motionEye |

### Keep (label changes applied 2026-11-09, user OK)

- No change: #142, #279, #232, #413, #192
- #165 feature → enhancement (HEAD exists, `handlers/base.py:295`; Content-Type of HEAD on pictures still missing, unverified at runtime)
- #277 feature → enhancement, +motion; #179 +motion; #258 +Raspberry Pi; #190 +motion (no overlay in recordings, so kept)

Clusters: bulk delete (#232 ← #184), pause all cameras (#192 ← #388), bulk download (#279). Unverified: whether the "One Picture" still is attached to the notification email (#363/#277).
