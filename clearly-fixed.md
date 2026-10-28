# Open issues that are clearly already resolved

- Surveyed: 2026-10-26 (base: `dev@upstream` = `d00f8a8b`), 914 open issues
- Scope: issues whose resolution is obvious to anyone **without reproducing a bug**
  (feature already present, requested doc page gone/replaced). Bugs that need a repro are out of scope here.
- Method (**verified**):
  1. All 914 open issues: listed cross-references from merged PRs / commits (GraphQL) → 22 issues
  2. Doc-related issues: title keywords (wiki, readme, docs, install instructions, translation, ...) + `documentation` label → 17 issues
  3. Read each candidate thread and checked the current `dev` code / current wiki (`motioneye.wiki.git`, last commit `d9686a1` 2026-10-19)
- Close pace: **about two actions per day** together with own PR activity (loose, not a quota), always with a comment explaining why (avoid the 2021 bulk-close backlash, see #1671)

## Close candidates

| Order | # | Title | Why it is resolved (evidence) | Status |
|---|---|---|---|---|
| 1 | [#1497](https://github.com/motioneye-project/motioneye/issues/1497) | Dots not allowed in filenames as of 0.41 | Fixed by #1502 (merged 2019-10-21). `static/js/main.js:17-18` `filenameValidRegExp`/`dirnameValidRegExp` include `.`; `cam.1/snap` and `name.with.dots` match (checked with Python `re`) | **closed 2026-10-25** ([comment](https://github.com/motioneye-project/motioneye/issues/1497#issuecomment-6400082807)) |
| 2 | [#657](https://github.com/motioneye-project/motioneye/issues/657) | Allow user to override hostname | Implemented by #846 (merged 2018-03-29) as the `server_name` setting: `settings.py:148`, `extra/motioneye.conf.sample` (`#server_name motionEye`), used in `handlers/main.py:36`; `load_settings()` picks it up (checked in container) | **closed 2026-10-26** ([comment](https://github.com/motioneye-project/motioneye/issues/657#issuecomment-6405145004)) |
| 3 | [#1094](https://github.com/motioneye-project/motioneye/issues/1094) | Removing old files on Google Drive | Implemented by #1118 (merged 2019-02-07): `GoogleDrive.clean_cloud` (`uploadservices.py:469`), triggered from `mediafiles.py:245`, UI switch `cleanCloudEnabledSwitch` (`templates/main.html:445`); remaining custom-period bug tracked in #1463 | **closed 2026-10-26** ([comment](https://github.com/motioneye-project/motioneye/issues/1094#issuecomment-6414555492)) |
| 4 | [#353](https://github.com/motioneye-project/motioneye/issues/353) | Wrong installation guide for Raspberry Pi 2 Raspbian | Wiki page `Install-On-Raspbian` deleted by MichaIng on 2025-12-16 (`d9f4147`); wiki sidebar "Installation" now links to the README instructions | **closed 2026-10-26** ([comment](https://github.com/motioneye-project/motioneye/issues/353#issuecomment-6415279757)) |
| 5 | [#284](https://github.com/motioneye-project/motioneye/issues/284) | Wiki info misleading for motion 3.4 / ffmpeg 3.0.2 on Jessie | Same: per-distro wiki install pages deleted 2025-12-16; README is the single install method | **closed 2026-10-27** ([comment](https://github.com/motioneye-project/motioneye/issues/284#issuecomment-6428548381)) |
| 6 | [#1356](https://github.com/motioneye-project/motioneye/issues/1356) | Raspbian wiki instructions (Buster deps) | Same: `Install-On-Raspbian*` pages deleted 2025-12-16 | **closed 2026-10-27** ([comment](https://github.com/motioneye-project/motioneye/issues/1356#issuecomment-6428643823)) |
| 7 | [#1459](https://github.com/motioneye-project/motioneye/issues/1459) | Are the Ubuntu install instructions correct? (`cp .../motioneye.conf.sample` fails) | Ubuntu wiki pages deleted 2025-12-16; README now uses `motioneye_init`, which installs the config itself (`extra/linux_init:77`) | **closed 2026-10-27** ([comment](https://github.com/motioneye-project/motioneye/issues/1459#issuecomment-6439345900)) |
| 8 | [#2746](https://github.com/motioneye-project/motioneye/issues/2746) | Install doc change: pillow on Bullseye (`pip2`) | `Install-on-Raspbian-Bullseye` deleted 2025-12-16 (`3a77b5b`); Python 2 instructions no longer exist. MichaIng already pointed to the README in 2023 | **closed 2026-10-27** ([comment](https://github.com/motioneye-project/motioneye/issues/2746#issuecomment-6439380015)) |
| 9 | [#3057](https://github.com/motioneye-project/motioneye/issues/3057) | Update wiki for Raspbian | MichaIng (2024-10-03): "most of those individual pages can be just removed" → done 2025-12-16 | **closed 2026-10-28** ([comment](https://github.com/motioneye-project/motioneye/issues/3057#issuecomment-6459250258)) |
| 10 | [#2232](https://github.com/motioneye-project/motioneye/issues/2232) | Pull request for wiki (Install-On-Raspberry-Pi) | The pages the proposal changed (`Installation`, Raspbian pages) were deleted 2025-12-16; installation lives in the README | candidate |
| 11 | [#1338](https://github.com/motioneye-project/motioneye/issues/1338) | Wiki contribute: Arch install via AUR | `Install-On-Arch` deleted 2025-12-16 (`5024bf3`); per-distro install pages are no longer kept. Weaker than the others (a request, not a fix) — close last or skip | candidate (weak) |

### Close comment drafts

- #1497: `This was fixed by #1502: dots are allowed in file and directory names since then (see filenameValidRegExp / dirnameValidRegExp in static/js/main.js). Closing as completed.`
- #657 (posted): `This has been implemented by @hobbyquaker in #846 (merged in 2018) as the server_name option ... Closing as completed.`
- #1094 (posted): `This has been implemented by @bob-lee in #1118 (merged in 2019) as the "Clean Cloud" option ... tracked in #1463. Closing as completed.`
- Wiki-page issues (#353, #284, #1356, #1459, #2746, #3057, #2232, #1338):
  `The per-distribution installation pages have been removed from the wiki (December 2025). There is now a single install method for all distributions in the README: https://github.com/motioneye-project/motioneye#installation. Closing, as the page this refers to no longer exists. If the README instructions do not work for you, please open a new issue.`

## Checked and NOT resolved (keep open)

| # | Why it stays open |
|---|---|
| #877, #1076 | `mosquitto-clients` was added to the old Docker image by #1077 (2018), but the current `docker/Dockerfile` does not install it |
| #2411 | Asks to skip `fdisk` in containers; `diskctl.py` still falls back to `fdisk -l` and the Dockerfile installs `fdisk` (#2410 went the other way) |
| #3393 | RAID (`md`) mounts: #3380 only dropped the write filter; MD devices are still not treated as partitions (discussion 2026-07) |
| #1248 | `manual_record`: #2691 added eventstart/eventend actions, but MichaIng's draft #3468 removes the manual recording mode — wait for it |
| #2592 | External gating signal: #2594 (percent settings) is unrelated |
| #2659 | Wiki Home still has the PayPal donation link (`Home.md:5-6`) |
| #2775 | `main.js:716` still concatenates the Clean Cloud warning instead of using a placeholder |
| #1852 | Arch: camera not working — a bug report, needs a repro |
| #2613, #3007 | Docker docs: `Install-In-Docker` deleted, but `docker/README.md` is still outdated → tracked by #3248 |
| #3244 | Configuration docs are still incomplete (MichaIng 2025-12-16) |
