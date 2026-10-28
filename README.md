# motionEye 作業メモ (triage ブランチ)

`motioneye-project/motioneye` での着手状況・進捗・調査結果を自分用に管理するブランチ。
**PR は出さない。** 本体コードとは独立した orphan ブランチ (`root()` から作成)。

## 運用

- 置き場所: fork (`origin` = `JamBalaya56562/motioneye`) の `triage` ブランチ
- 編集: `jj new triage` → ファイル更新 → `jj describe` → `jj bookmark set triage -r '@'` → `jj git push --bookmark triage`
- 作業に戻る: `jj new 'trunk()'`
- 調査結果には根拠の種類を付ける: **検証済み / ドキュメント根拠 / 推測**

## PR の出し方 (ルール)

- **出す PR は常に 1 本だけ。** 2 本目は、1 本目がマージかクローズされてから出す
  - 理由: メンテナーは慎重にレビューするので、同時に何本出してもレビューされるのは結局 1 本ずつ。並べても早くならない
- 逆に、**PR が 1 本も出ていない状態は作らない。** 1 本目が閉じたら次をすぐ出せるよう準備しておく
- PR のレビューを待っている間は、**issue の triage 作業**をする
- 着手中・準備中の PR は下の「PR 状況」に記録する

## Issue close rules

- Pace: **about five actions per day** (closes and own PR activity combined; raised from two on 2026-10-27 as no pushback was seen), not a strict quota — the point is to go slowly enough that maintainers do not push back (a bulk close in 2021 drew backlash, see #1671)
- Always close with a comment explaining why
- Bugs: close only after confirming they no longer reproduce. Issues that are obviously resolved without a repro (feature exists, doc page gone) can be closed with the reason
- Each close needs the user's OK on the comment first

## PR 状況

| 状態 | ブランチ | issue | PR | メモ |
|---|---|---|---|---|
| Merged 2026-10-25 (squash `5acdd519`, by MichaIng) | `feat/motion-control-auth` (deleted) | #1671 (closed) | [#3474](https://github.com/motioneye-project/motioneye/pull/3474) | Done |
| Merged 2026-10-26 (`429bae74`, by MichaIng) | `enh/conf-root-owned` (deleted) | — (follow-up of #3474) | [#3475](https://github.com/motioneye-project/motioneye/pull/3475) | Done |
| Merged 2026-10-28 (`979cfac1`) | `enh/no-pid-file` | #2540 (related, not closing) | [#3478](https://github.com/motioneye-project/motioneye/pull/3478) | — |
| Open, in review (submitted 2026-10-28) | `enh/docker-puid` (fork, `d8c5b8c5`) | #3181 | [#3484](https://github.com/motioneye-project/motioneye/pull/3484) | Reworked to `docker run --user` after MichaIng's comment; waiting for review |
| Open, in review (submitted 2026-10-28) | `fix/layout-rows` (fork, `a9a22942`) | #2583 (supersedes #2590) | [#3485](https://github.com/motioneye-project/motioneye/pull/3485) | Waiting for review. Screenshots are GitHub attachments (fork branch `pr-assets-layout-rows` no longer needed) |
| Prepared, not submitted | `fix/mask-conf-path` (fork, `169bd99d`, on dev) | — (found while reproducing #2755) | — | Mask files written to the default CONF_PATH instead of the configured one since #3324 (0.44.0). Submit when a PR slot is free. PR text: [pr-drafts.md](pr-drafts.md) |
| Prepared, not submitted | `fix/mask-grid` (fork, `eda341ae`, on dev) | #2755 | — | Mask editor grid at the capture size instead of the dimmed preview. Screenshots still to upload as GitHub attachments. PR text: [pr-drafts.md](pr-drafts.md) |

## Follow-up ideas (next PR candidates)

| Idea | Source | Notes |
|---|---|---|
| `motioneye.conf` owned by `root:motion` with mode `0640`, so the motionEye server cannot lift its own restrictions (auth, `webcontrol_*`) | MichaIng on [#3474](https://github.com/motioneye-project/motioneye/pull/3474) (2026-10-25) | Needs a different mode check: warn if anyone but root and motionEye can read it, `chmod` only when writable, otherwise tell the admin to fix it. Dedicated PR → **submitted as [#3475](https://github.com/motioneye-project/motioneye/pull/3475)** |
| motion's `config/write` still works with `webcontrol_parms 0` (writes the running config to disk) | Observed with motion 4.5.1 (2026-10-26) | Not reported anywhere yet; check whether it matters |

## 前提 (2026-10-25 時点)

- upstream への権限: `push:true, triage:true` (admin/maintain は無し)。issue のクローズ・ラベル付けが可能
- issue のクローズ時期: **PR が dev にマージされた時点** (リリース待ちではない)。既定ブランチが `dev` なので `Fixes #xxx` がマージ時に効く。
  マイルストーンは「どのリリースに入るか」の目印 (v0.44.0 / v0.45.0 の closed issue のクローズ時刻で確認、検証済み)
- GitHub Projects は org・repo とも無効。メンテナー (Marijn0) の指示は **v0.45.0 マイルストーンの open issue から着手**
  ([#3387 のコメント](https://github.com/motioneye-project/motioneye/pull/3387#issuecomment-6151590452))

## ドキュメント一覧

| ファイル | 内容 |
|---|---|
| [milestone-v0.45.0.md](milestone-v0.45.0.md) | v0.45.0 未完了 issue の整理 (着手しやすさ・影響度・議論状況) |
| [clearly-fixed.md](clearly-fixed.md) | Open issues that are clearly already resolved (close candidates) |
| [close-candidates-pi.md](close-candidates-pi.md) | Close candidates, round 2: Raspberry Pi issues (some need a check on the real Pi) |

## 進捗ログ

| 日付 | 内容 |
|---|---|
| 2026-10-25 | jj で `upstream` を追加、`dev@upstream` を track、`trunk()` = `dev@upstream` |
| 2026-10-25 | v0.45.0 マイルストーンの未完了 19 件を整理 → milestone-v0.45.0.md |
| 2026-10-25 | #2828 をクローズ (#3376 で修正済み、closing 参照漏れ) |
| 2026-10-25 | PR は常に 1 本だけ出し、レビュー待ちの間は triage をするルールを追加 |
| 2026-10-25 | #1671 を `feat/motion-control-auth` で実装 (339 tests passed、実 motion 4.5.1 で 401/200 を確認) |
| 2026-10-25 | #1671 の PR [#3474](https://github.com/motioneye-project/motioneye/pull/3474) を提出 → レビュー待ちの間は triage |
| 2026-10-26 | #3474: Marijn0 review → restrict `motioneye.conf` to 0600 (commit `3351042f`, 342 tests passed), replied |
| 2026-10-26 | Surveyed clearly-resolved open issues → 11 close candidates in clearly-fixed.md |
| 2026-10-25 | Closed #1497 (fixed by #1502). Close pace relaxed to about two actions per day |
| 2026-10-26 | #3474: MichaIng review → linux_init chmod 0600, sample note, `webcontrol_parms` default 0 (commit `1795f4b2`, 344 tests passed, verified with motion 4.5.1) |
| 2026-10-25 | #3474 merged by MichaIng (squash `5acdd519`), #1671 closed. Fork `dev` fast-forwarded to `5acdd519` |
| 2026-10-26 | Prepared the `root:motion` 0640 follow-up on `enh/conf-root-owned` (348 tests passed, checked with real owners/modes in a container); PR not submitted yet |
| 2026-10-26 | Submitted the follow-up as [#3475](https://github.com/motioneye-project/motioneye/pull/3475) |
| 2026-10-26 | Closed #657 (implemented by #846 as `server_name`). Next candidate: #1094 |
| 2026-10-26 | #3475: MichaIng review → 0600 when motionEye owns the file, suggest `root:<GID>` 0640 otherwise. Applied with fixes for two bugs in the suggestions (`{guid}` NameError, `0x030` instead of `0o030`) and the group check for root-owned files kept (commit `c06c4319`, 349 tests passed, checked with the motion user); PR body updated |
| 2026-10-26 | Reviewed and approved #3476 (free-cup-holder-exe, per-camera certificate check; 380 tests passed together with #3475) |
| 2026-10-26 | Closed #1094 (implemented by #1118 as Clean Cloud; follow-up bug #1463 stays open). Next candidates: wiki-page issues (#353 first) |
| 2026-10-26 | #3196: verified with real CIFS mounts that foreign mounts are not unmounted; asked MichaIng whether a case is missing ([comment](https://github.com/motioneye-project/motioneye/issues/3196#issuecomment-6414866676)). Not closed |
| 2026-10-26 | Prepared #2540 on `enh/no-pid-file`: motion tracked by its `Popen` handle, no `motion.pid`; `run_path` only checked with `-b` (353 tests passed, real motion as non-root without run_path). Not submitted |
| 2026-10-26 | Closed #353 (wiki `Install-On-Raspbian` deleted 2025-12-16, README is the single install method). Next candidate: #284 |
| 2026-10-26 | #3475 merged by MichaIng (`429bae74`); #3476 (free-cup-holder-exe) merged (`f623690a`) |
| 2026-10-27 | Rebased `enh/no-pid-file` onto `f623690a` (389 tests passed) and submitted it as [#3478](https://github.com/motioneye-project/motioneye/pull/3478) |
| 2026-10-27 | #3478: pre-commit bandit B607 (`Popen(['sleep', ...])` in a test) → use `sys.executable` like the other tests; squashed into the single commit `d839e825` (bandit clean, motionctl tests passed) |
| 2026-10-27 | Closed #284 (wiki `Install-On-Debian` deleted 2025-12-16; `motioneye_init` installs pre-built motion and distro ffmpeg). Next candidate: #1356 |
| 2026-10-27 | Close pace raised to about five actions per day (no pushback so far) |
| 2026-10-27 | Closed #1356 (wiki `Install-On-Raspbian*` deleted 2025-12-16). Next candidate: #1459 |
| 2026-10-27 | #3478: MichaIng review → dropped `RuntimeDirectory`/`LogsDirectory` from the systemd unit + inline `IOLoop.current().add_callback` nit (commit `5df7d585`, 389 tests passed, starts without `/run/motioneye` and `/var/log/motioneye`); replied "Thanks, done." inline |
| 2026-10-27 | Closed #1459 (wiki Ubuntu install pages deleted 2025-12-16; `motioneye_init` copies the config sample itself). Next candidate: #2746 |
| 2026-10-27 | Closed #2746 (wiki `Install-on-Raspbian-Bullseye` deleted 2025-12-16; README is Python 3 and lists the ARMv6 Pillow build deps). Next candidate: #3057 |
| 2026-10-26 | #3196 closed by MichaIng after the real-mount check (missed the `motioneye_` prefix check) |
| 2026-10-27 | MichaIng added #800 and #1047 (features) to v0.45.0 on 2026-10-26 |
| 2026-10-27 | Prepared #3181 on `enh/docker-puid` (PUID/PGID at container start, RUN_UID/RUN_GID dropped; built the image and checked default root, switch to 1000, restart, invalid value; shellcheck with CI flags). Not submitted |
| 2026-10-27 | Prepared #2583 on `fix/layout-rows`: rows dropped from the layout width in a25dec20 (2018); divide by rows again, count frame padding, record the picture ratio on load. Before/after screenshots + measurements (Playwright, 1920x1080 and 1366x768). Not submitted |
| 2026-10-27 | Policy: an issue in the milestone counts even if someone else's PR exists; take over PRs idle for years without asking (credit + "Supersedes") |
| 2026-10-28 | #3478 merged (`979cfac1`). Rebased `enh/docker-puid` onto dev `a8390113` (no conflicts), rebuilt the image and re-ran the checks (default root, switch to 1000 with meyectl as uid 1000, restart without chown -R, invalid PUID; shellcheck clean); submitted as [#3484](https://github.com/motioneye-project/motioneye/pull/3484) |
| 2026-10-28 | Up to two open PRs from now on (user). Rebased `fix/layout-rows` onto `a8390113` and submitted it as [#3485](https://github.com/motioneye-project/motioneye/pull/3485) (assignee, v0.45.0, `bug` + `JavaScript`). Replaced the raw fork image URLs with GitHub attachments uploaded by pasting in the in-app browser. test_install ubuntu-22.04-arm failed: meyectl logged nothing within 11 s (the passing jobs listen after ~3 s; the PR only changes `main.js`), so the failed jobs were re-run |
| 2026-10-28 | #3484 reworked on MichaIng's suggestion: run as the `docker run --user` user instead of PUID/PGID (no su/chown/passwd edits; sample 0644, copied 0600; volume dirs dropped from the image, as an empty volume otherwise took their 100:101 owner on every mount). Checked default root, upgrade from dev volumes, --user on fresh volumes (fails as documented), after the README chown (1000:1000 for meyectl, motion and 22 snapshots), bind mounts; pushed `d8c5b8c5`, updated title/body and replied |
| 2026-10-28 | #3485 review (MichaIng): rebased onto dev `5dc324ed`; removed the ratio update in `refreshCameraFrames()` (its fallback of 1 had kept a failed camera fitting: without it a failed 16:9 camera overflowed to 1241 px), so `onerror` sets the placeholder's 0.75 and the layout updates on entering/leaving the error (950 px, back to 1075 px). Padding measured identical for 4:3/16:9/1:1 (12.78 px at 22 px font, 9.38 px at 16 px; border rounded 4.4→4 px). Pushed `a9a22942`, body updated, replied on comment 1; reply on comment 2 (keeps measuring) awaits the user's OK |
| 2026-10-28 | Closed #3057 (wiki Raspbian install pages deleted 2025-12-16, as MichaIng suggested in 2024). Next candidate: #2232 |
| 2026-10-28 | Closed #2232 as not planned (wiki change proposal for pages deleted 2025-12-16). Pace of five a day is a loose guide (user). Next candidate: #1338 (weak) |
| 2026-10-28 | #1338 kept open (user, option B): AUR install is a proposal that the wiki removal does not settle; Arch has no automatic deps in `motioneye_init`; later together with #1852 (neither in the milestone). The close candidate list is now done |
| 2026-10-28 | Prepared #3066 on `enh/venv` (`f39efa29`, fork, not submitted): `linux_init --meyectl`, `motioneye_init` passes its environment's meyectl, README + test_install use a venv in /opt/motioneye. Checked 5 scenarios in a systemd container (venv, explicit path, invalid path, system-wide, migration); fork CI all green (test_install 6/6, pre-commit after a bandit B103 fix in the new test) |
| 2026-10-28 | Round 2 close survey: Raspberry Pi issues (103 by title, 36 read) → 10 closable without repro, 8 libcamera duplicates (check the wiki libcamerify steps on the real Pi first), 2 install issues to check on the Pi → close-candidates-pi.md. Not closing yet (user) |
| 2026-10-28 | Real Pi check over SSH (Pi 5, trixie 64-bit, Camera Module 3): README install works but get-pip fails with externally-managed-environment (fixed by enh/venv); wiki libcamerify works; default 320x240 gives a green band (stride 384), 640x480 is fine (same as #3116) |
