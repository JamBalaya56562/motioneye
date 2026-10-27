# v0.45.0 マイルストーン 未完了 issue 整理

- 調査日: 2026-10-25 (基準: `dev@upstream` = `d00f8a8b`)
- マイルストーン: https://github.com/motioneye-project/motioneye/milestone/3 (期日なし、open 21 / closed 104)
- 未完了一覧: https://github.com/motioneye-project/motioneye/issues?q=is%3Aissue+state%3Aopen+milestone%3Av0.45.0
- 根拠: 19 件の本文・全コメント・cross-reference を `gh` で取得して確認、dev のコードを grep で確認 (**検証済み**)。
  「着手しやすさ」「影響度」の評価は **推測**
- マイルストーン内の open PR: #3468 (MichaIng, draft, 手動録画モード削除), #3447 (Weblate)

## 状態の凡例

`未着手` / `調査中` / `実装中` / `PR中 (#番号)` / `完了` / `見送り`

## 推奨着手順

| 順 | # | 理由 | 状態 |
|---|---|---|---|
| 1 | #2828 | dev で修正済み。クローズするだけ | 完了 (2026-10-25 クローズ) |
| 2 | #1671 | MichaIng が実装手順を提示済み。小規模・セキュリティ | 完了 (#3474 merged 2026-10-25) |
| 3 | #3196 | 外部 CIFS マウントは外されないと実マウントで検証 → MichaIng 同意、クローズ | 完了 (2026-10-26 MichaIng がクローズ) |
| 4 | #3248 + #3007 | Docker ドキュメント。コードリスクなし | 未着手 |
| 5 | #2755 残り / #2540 | 余力があれば | 未着手 |

---

## A. すぐ片付くもの

| # | 内容 | 状況 | 次の一手 | 状態 |
|---|---|---|---|---|
| [#2828](https://github.com/motioneye-project/motioneye/issues/2828) | Dropbox - Service error | **dev で修正済み (検証済み)**: 自分の [#3376](https://github.com/motioneye-project/motioneye/pull/3376) が 2026-06-28 マージ。`motioneye/uploadservices.py:666` が `json.dumps(body).encode()` | #3376 を添えてクローズ | 完了: 2026-10-25 クローズ ([コメント](https://github.com/motioneye-project/motioneye/issues/2828#issuecomment-6398775706))。#3376 の closing 参照が #2940 になっていたため自動クローズされなかった |
| [#2755](https://github.com/motioneye-project/motioneye/issues/2755) | 検知マスクが時間とともにずれる | 一部修正: [#3470](https://github.com/motioneye-project/motioneye/pull/3470) が 2026-10-22 19:23 マージ → 直後 19:24 に MichaIng「resolution dimmer 使用時はまだ未解決」 | dimmer < 100% で再現 → 修正。Marijn0 の再現手順・ログ (`editable mask needs resizing from 819x614 to 1024x768`) あり。zagrim 案: DOM サイズでなく `resolutionFactor` と実フレームサイズでスケーリング | 未着手 |

## B. 方針合意済み・実装待ち

| # | 内容 | 着手しやすさ | 影響度 | 議論状況 | 状態 |
|---|---|---|---|---|---|
| [#1671](https://github.com/motioneye-project/motioneye/issues/1671) | motion control port への認証付き接続 | ◎ | 中 (security) | 2026-05-21 MichaIng が実装手順を提示: `settings.py` に username/password 設定 (既定空)、`extra/motioneye.conf.sample` 追記、`config.py` で `webcontrol_auth_method`/`webcontrol_authentication` を出力、`motionctl.py` の control API リクエストに認証を付与。dev には `webcontrol_auth*` の出力なし (grep で確認) | 完了 (#3474 merged 2026-10-25) |
| [#3196](https://github.com/motioneye-project/motioneye/issues/3196) | motionEye が追加した CIFS マウントだけを扱う | ○ | 中〜高 | 2025-12-13 MichaIng が原因特定: `controls/smbctl.py` の `update_mounts` が起動時にカメラ未使用の CIFS マウントを全部外す、`_umount_all` が停止時に全 CIFS を外す (`server.py` から呼ばれる)。方針: motionEye が付けたものだけ外す | 完了: 2026-10-26 MichaIng「`motioneye_` 接頭辞の確認を見落としていた、問題ない」としてクローズ |
| [#2540](https://github.com/motioneye-project/motioneye/issues/2540) | Docker 非 root で PID ファイルを書けない | ○ | 中 | 2023-03 MichaIng「PID ファイル無しで動ける選択肢が最善」。dev は常に `RUN_PATH/motioneye.pid` を書く (`server.py:528`) | #3478 マージ済み (2026-10-28, Related to #2540)。Docker `--user` は entrypoint の `su` が残るため #3181 側 |
| [#3364](https://github.com/motioneye-project/motioneye/issues/3364) | 0.44 で「remember me」が消えた | △ | **高** (kiosk/PWA/HA の後退) | セッション期間は [#3410](https://github.com/motioneye-project/motioneye/pull/3410) (Marijn0, 2026-09-02 マージ) で設定可能に (`normal_session_expiry_hours`)。残り: ①PWA で `SameSite=Strict` cookie が送られない (`handlers/login.py:282`)、Lax にするなら別の CSRF 対策要検討 ②Tornado の cookie 機能 (`get_secure_cookie` の max age) で remember me を復活する案 (MichaIng)。セキュリティ設計判断が必要 | 未着手 |

## C. ドキュメント

| # | 内容 | 議論状況 | 状態 |
|---|---|---|---|
| [#3248](https://github.com/motioneye-project/motioneye/issues/3248) + [#3007](https://github.com/motioneye-project/motioneye/issues/3007) | Docker インストール手順 | ほぼ重複。`docker/README.md` に `ccrisan/motioneye:master-amd64` が残存 (確認済み)。MichaIng の推奨 `docker run` 例 (2026-02-11, `motioneyeproject/motioneye`, `/etc/motioneye` と `/var/lib/motioneye` を volume, `--restart unless-stopped`)。Docker Hub と GHCR はどちらでも可。main README に Docker 手順を統合する方針。NVENC は host に NVIDIA container toolkit + motion 側の preset 問題 (motion v5 で修正)。MarcelCoding 案: wiki を repo の `docs/` に移して MkDocs 化 | 未着手 |
| [#3066](https://github.com/motioneye-project/motioneye/issues/3066) | install 手順と systemd unit を venv へ | README だけでなく `extra/linux_init` で `meyectl` パスを自動検出 (PATH or `motioneye_init` と同じディレクトリ、または引数で渡す) + install テスト更新が必要。MichaIng の DietPi 手順 (2026-02-22): `python3 -m venv /opt/motioneye` → `pip install motioneye` → `motioneye_init` → service の `ExecStart` を書換 | 未着手 |

## D. Docker / 非 root (まとめて設計)

| # | 内容 | 議論状況 | 状態 |
|---|---|---|---|
| [#3181](https://github.com/motioneye-project/motioneye/issues/3181) | PUID/PGID 対応 | MichaIng 同意: `RUN_UID`/`RUN_GID` (build arg, `docker/Dockerfile:5`) を実行時の PUID/PGID に置き換え。既定は root のままでよいという立場 | PR中 ([#3484](https://github.com/motioneye-project/motioneye/pull/3484), Fixes #3181) |
| [#2407](https://github.com/motioneye-project/motioneye/issues/2407) | Docker を motion ユーザーで実行 | 本文はほぼ空。#2388 の議論参照 | 未着手 |
| [#2710](https://github.com/motioneye-project/motioneye/issues/2710) | 非 root で SMB マウント | 本文はメモ程度 (グループ/capabilities で可能) | 未着手 |

#2540 と合わせて「非 root 運用」として 1 本にまとめるのがよさそう (推測)。

## F. 2026-10-26 にマイルストーン追加 (MichaIng, label feature)

| # | 内容 | 状態 |
|---|---|---|
| [#800](https://github.com/motioneye-project/motioneye/issues/800) | API で動体検知をオン/オフ (motionEye と同期、通知も) | 未着手 |
| [#1047](https://github.com/motioneye-project/motioneye/issues/1047) | 検知・録画を外部から発火 (eventstart/eventend action は #2691 でマージ済み) | 未着手 |

## E. 重い / ハードウェア必要 / 原因不明

| # | 内容 | 状況 | 状態 |
|---|---|---|---|
| [#2425](https://github.com/motioneye-project/motioneye/issues/2425), [#2683](https://github.com/motioneye-project/motioneye/issues/2683), [#2812](https://github.com/motioneye-project/motioneye/issues/2812) | libcamera / Camera Module 3 | 計 160 コメント超、影響最大。本筋は [#2765](https://github.com/motioneye-project/motioneye/pull/2765) (strips, libcamerify 対応 PR, 2023〜open, 2026-10-20/21 にも議論)。MichaIng の未決事項: motionEye 全体 (`meyectl`) を libcamerify で包む (v4l2-ctl も shim を見る) か motion だけか。現状の回避策: `ExecStart=/usr/bin/libcamerify /usr/local/bin/meyectl`。実機 (Pi + カメラ) が必要 | 未着手 |
| [#2887](https://github.com/motioneye-project/motioneye/issues/2887) | 録画冒頭 3 秒フリーズ | 0.43 からの後退報告。pre_capture / minimum motion frames / passthrough を試しても未解決。motion 側の可能性あり | 未着手 |
| [#2516](https://github.com/motioneye-project/motioneye/issues/2516) | Google Drive にファイルが上がらない | 2024-08 指摘: Google の OOB 廃止で新しい OAuth フローが必要。規模大 | 未着手 |
| [#1810](https://github.com/motioneye-project/motioneye/issues/1810) | SMB 上のメディアを GUI から削除できない | 原因: `.keep` が SMB で隠しファイル扱いになりディレクトリ削除が失敗。MichaIng は `.keep` の必要性自体に疑問、方針未決 | 未着手 |
| [#2583](https://github.com/motioneye-project/motioneye/issues/2583) | プレビューがウィンドウに収まらない | [#2590](https://github.com/motioneye-project/motioneye/pull/2590) (lowlyocean) が 2022〜open、**conflict 中**、zagrim approve 済み。assignee は @lowlyocean。引き継ぐなら一声かける | PR中 ([#3485](https://github.com/motioneye-project/motioneye/pull/3485), Fixes #2583)。#2590 (2022 から停止) を引き継ぎ (Supersedes) |
