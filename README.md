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

## PR 状況

| 状態 | ブランチ | issue | PR | メモ |
|---|---|---|---|---|
| レビュー待ち | `feat/motion-control-auth` | #1671 | [#3474](https://github.com/motioneye-project/motioneye/pull/3474) | 2026-10-25 提出。closing 参照 = #1671 を確認済み |

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

## 進捗ログ

| 日付 | 内容 |
|---|---|
| 2026-10-25 | jj で `upstream` を追加、`dev@upstream` を track、`trunk()` = `dev@upstream` |
| 2026-10-25 | v0.45.0 マイルストーンの未完了 19 件を整理 → milestone-v0.45.0.md |
| 2026-10-25 | #2828 をクローズ (#3376 で修正済み、closing 参照漏れ) |
| 2026-10-25 | PR は常に 1 本だけ出し、レビュー待ちの間は triage をするルールを追加 |
| 2026-10-25 | #1671 を `feat/motion-control-auth` で実装 (339 tests passed、実 motion 4.5.1 で 401/200 を確認) |
| 2026-10-25 | #1671 の PR [#3474](https://github.com/motioneye-project/motioneye/pull/3474) を提出 → レビュー待ちの間は triage |
