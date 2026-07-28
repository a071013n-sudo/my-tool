# apps フォルダの使い方

## 新しいアプリを追加する手順

1. `apps/` の下に、アプリごとのフォルダを作る
   例: `apps/thumbnail-viewer/`

2. そのフォルダに以下の2つを入れる
   - サムネイル画像 (例: `thumbnail.png` / `.jpg` など、ファイル名は自由)
   - 配布ファイル本体 (例: `thumbnail-viewer.zip`)

3. `apps/apps.json` に1件追記する

```json
{
  "name": "サムネイルビューアー",
  "description": "提出物のサムネイルを出席番号順に並べて確認できます。",
  "thumbnail": "apps/thumbnail-viewer/thumbnail.png",
  "file": "apps/thumbnail-viewer/thumbnail-viewer.zip",
  "fileLabel": "thumbnail-viewer.zip (1.2MB)"
}
```

JSON は配列なので、複数件のときは `,` で区切って追加してください。

## 注意点

- GitHub は 1ファイルあたり **100MB** が上限です（50MB を超えると警告が出ます）。
  大きな実行ファイルは、GitHub の **Releases** 機能でアップロードし、
  `file` の値をそのダウンロードURL
  （例: `https://github.com/ユーザー名/リポジトリ名/releases/download/v1.0/tool.zip`）
  に置き換えると、リポジトリを圧迫せずに配布できます。
- リポジトリを **Public** にしないと、GitHub Pages 上で誰でもダウンロードすることはできません。
- 個人情報や学校の内部資料など、公開してはいけないファイルは
  絶対にこのフォルダに置かないでください（Public リポジトリは世界中から見えます）。
