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

- Pace: **about two actions per day** (closes and own PR activity combined), not a strict quota — the point is to go slowly enough that maintainers do not push back (a bulk close in 2021 drew backlash, see #1671)
- Always close with a comment explaining why
- Bugs: close only after confirming they no longer reproduce. Issues that are obviously resolved without a repro (feature exists, doc page gone) can be closed with the reason
- Each close needs the user's OK on the comment first

## PR 状況

| 状態 | ブランチ | issue | PR | メモ |
|---|---|---|---|---|
| Merged 2026-10-25 (squash `5acdd519`, by MichaIng) | `feat/motion-control-auth` (deleted) | #1671 (closed) | [#3474](https://github.com/motioneye-project/motioneye/pull/3474) | Done |
| Merged 2026-10-26 (`429bae74`, by MichaIng) | `enh/conf-root-owned` (deleted) | — (follow-up of #3474) | [#3475](https://github.com/motioneye-project/motioneye/pull/3475) | Done |
| Open, in review (submitted 2026-10-27) | `enh/no-pid-file` (fork, `16d59197`) | #2540 (related, not closing) | [#3478](https://github.com/motioneye-project/motioneye/pull/3478) | Waiting for review; triage meanwhile |

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
| [clearly-fixed.md](clearly-fixed.md) | Open issues that are clearly already resolved (close candidates, one per day) |

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
