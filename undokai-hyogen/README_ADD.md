# README に追記する内容

## ファイルの役割（表に追記）

| ファイル | 役割 | 編集 |
| --- | --- | --- |
| `content/undokai/*.json` | 運動会の資料の中身 | **ここだけ編集** |
| `undokai-hyogen/*.html` | 運動会の資料（22演目＋一覧） | 自動生成。手で触らない |
| `undokai-hyogen/sitemap.xml` | 検索エンジン向けの一覧 | 自動生成。手で触らない |
| `undokai-hyogen/undokai-guides.zip` | 一式まとめてダウンロード用 | 自動生成。手で触らない |
| `.github/scripts/build_undokai.py` | 資料の見た目と図の描画 | デザイン変更時 |
| `.github/workflows/undokai.yml` | 自動化の設定 | ほぼ触らない |

## 運動会の資料を直すとき

`content/undokai/` の中の JSON を編集してください。`undokai-hyogen/` の HTML は
編集しても、次の生成で上書きされます。

保存すると数分後に、22件の資料・sitemap・zip がまとめて作り直されます。

### 演目を1つ足すとき

既存の JSON から1件をコピーして、`id` と中身を書き換えてください。
`id` がそのままファイル名（`{id}.html`）になります。

足したあと、`undokai-hyogen/index.html` の `DATA` にも同じ `name` で1件足してください。
**名前が一致していないと生成が失敗します。** メールで「資料なし」「一覧なし」の
どちらかが通知されるので、そこを見て直してください。

### 図について

動きの姿勢図は、肩からの角度と長さで指定します。

```
"pose": { "aL":190, "aR":170, "lL":27, "lR":27, "stance":"toe",
          "prop":{ "type":"pom" } }
```

- 角度は `0` が真下、`90` が画面右、`180` が真上、`270` が画面左
- `stance` は `normal` / `wide` / `lunge` / `crouch` / `kneel` / `jump` / `toe` / `together`
- `prop.type` は `flag` / `pole` / `kasa` / `umbrella` / `board` / `pom` / `cloth` / `naruko` / `taiko` / `none`

隊形図は、グラウンド上の座標（横320・縦200）で指定します。

```
"groups": [[70, 58, 15, 8, 12, 12]]     // x, y, 列数, 行数, 横間隔, 縦間隔
"rings":  [[160, 105, 96, 52, 26]]      // 中心x, 中心y, 横半径, 縦半径, 人数
"arrows": [[48, 56, 268, 56]]           // x1, y1, x2, y2
```

## 権利について

資料には楽曲の著作権と組体操の安全に関する整理を入れてあります。
**法令や通知の内容が変わったら、必ず直してください。** 事実と違う記載が
残っていると、サイト全体の信頼が失われます。
