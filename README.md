# motionEye 作業メモ (triage ブランチ)

`motioneye-project/motioneye` での着手状況・進捗・調査結果を自分用に管理するブランチ。
**PR は出さない。** 本体コードとは独立した orphan ブランチ (`root()` から作成)。

## 運用

- 置き場所: fork (`origin` = `JamBalaya56562/motioneye`) の `triage` ブランチ
- 編集: `jj new triage` → ファイル更新 → `jj describe` → `jj bookmark set triage -r '@'` → `jj git push --bookmark triage`
- 作業に戻る: `jj new 'trunk()'`
- 調査結果には根拠の種類を付ける: **検証済み / ドキュメント根拠 / 推測**

## 前提 (2026-10-25 時点)

- upstream への権限: `push:true, triage:true` (admin/maintain は無し)。issue のクローズ・ラベル付けが可能
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
