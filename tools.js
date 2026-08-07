/* ==========================================================
   小学校の校務PCで使えるソフト ─ 掲載データ

   ★ 更新するのは、このファイルだけです。
     index.html と flyer.pdf は、ここを読んで表示・生成されます。

   GitHub の画面から直接編集できます（スマホからでも可）。
   保存すると数分後にチラシPDFが自動で作り直されます。
   ========================================================== */

/* サイト全体の情報 */
window.SITE = {
  name:      "小学校の校務PCで使えるソフト",
  lead:      "インストール不要で、オフラインで使えます。",
  lead2:     "校務PCでそのまま動くものを集めました。",
  url:       "https://a071013n-sudo.github.io/my-tool/",
  repo:      "https://github.com/a071013n-sudo/my-tool",
  flyerNote: "作成：現職の小学校教員　／　ご自由に印刷・回覧してください"
};

/* 安全性バンドの4項目（サイトとチラシの両方に出ます）
   ★全ツールで例外なく真であることだけを書いてください。
     1件でも当てはまらないものがあると、サイト全体の信頼が崩れます。 */
window.TRUST = [
  ["作成者にデータは届きません", "利用状況や入力内容を集めるサーバーを持っていません"],
  ["オフラインで動きます",       "ネットにつながっていない校務PCを前提に作っています"],
  ["広告・アクセス解析なし",     "Cookieも使っていません"],
  ["登録不要・すべて無料",       "このサイトへの会員登録は必要ありません"]
];

/* 種類と、その色 */
window.CATEGORY_COLOR = {
  "校務・事務":    "#5B8C56",
  "文書・表記":    "#3F8593",
  "ファイル整理":  "#A9762F",
  "行事":          "#9C5A45",
  "その他":        "#7A7F6B"
};

/* ==========================================================
   ▼ ツールを追加するときは、TOOLS の配列にオブジェクトを1つ足すだけです。

   必須は id / name / description の3つだけ。他は省略できます。

   id          : 半角英数字のID（URL共有 #tool=id に使われます）
   icon        : 画像がないときに表示する絵文字
   name        : ツール名
   category    : 種類。上の CATEGORY_COLOR のキーと合わせてください
   env         : 動かすのに必要なもの（一覧カードに出ます）
   tags        : タグ（詳細画面に出ます）
   summary     : 一覧カード用の短い説明（1〜3行）
   description : 詳細画面用の説明（改行はそのまま反映されます）
   updated     : 更新年月 "2026-08" 形式。新しい2件に NEW が付きます
   thumbnail   : 画像URL（空ならアイコンを表示）
   download    : ダウンロードURL
   repo        : リポジトリURL

   safety      : 先生方が一番気にする3点。必ず実態どおりに書いてください。
                 install / login / data の3項目で、それぞれ
                   lv … "ok"(緑=安心) / "note"(灰=条件あり) / "warn"(黄=要注意)
                   s  … カードに出る短い文
                   d  … 詳細画面に出る説明文
                 ※ここに事実と違うことを書くと、信頼を一度で失います。
   ========================================================== */

// ---- よく使う安全性の書き方は、まとめて使い回しています ----

// HTMLファイル形式のもの（ブラウザで開くだけ）
const SAFETY_HTML = {
  install: { lv:"ok", s:"インストール不要",
             d:"ダウンロードしたHTMLファイルをブラウザで開くだけです。校務PCに何かを入れる必要はありません。" },
  login:   { lv:"ok", s:"ログイン不要",
             d:"アカウントの作成やログインは必要ありません。" },
  data:    { lv:"ok", s:"外部送信なし",
             d:"入力した内容はパソコンの中だけで処理されます。ネットにつながっていない状態でも動きます。" }
};

// 実行ファイル(exe)形式のもの
const SAFETY_EXE = {
  install: { lv:"note", s:"exeを直接実行",
             d:"インストーラーはありません。ダウンロードしたファイルをそのまま実行します。初回起動時にWindowsの警告が出ることがあります。" },
  login:   { lv:"ok", s:"ログイン不要",
             d:"アカウントの作成やログインは必要ありません。" },
  data:    { lv:"ok", s:"外部送信なし",
             d:"処理はパソコンの中だけで行われます。ネットにつながっていない状態でも動きます。" }
};

window.TOOLS = [
  {
    id: "task_cho",
    icon: "🗒️",
    name: "タスク管理ソフト",
    category: "校務・事務",
    env: "ブラウザのみ",
    tags: ["インストール不要", "校務PCで使える", "HTMLファイル"],
    summary: "職員室で人気だった付箋ソフトの改良版。ドラッグでタスクを動かせて、繰り返しの設定もできます。",
    description: "Windows標準の付箋ソフトが職員室で人気だったので、改良版を作成。\nドラッグアンドドロップでタスクを移動したり、繰り返しの設定ができます。\nとても便利。",
    thumbnail: "images/task_cho.png",
    download: "https://github.com/a071013n-sudo/my-tool/releases/download/task_cho/task-cho.html",
    repo: "https://github.com/a071013n-sudo/my-tool",
    safety: SAFETY_HTML
  },
  {
    id: "timetable_gene",
    icon: "🗓️",
    name: "固定時間割ジェネレーター",
    category: "校務・事務",
    env: "ブラウザのみ",
    tags: ["インストール不要", "校務PCで使える", "HTMLファイル"],
    summary: "年度初めの固定時間割の案を3秒ほどで作ります。時間講師の条件も設定できます。",
    description: "担当になると年度初めの貴重な時間を吸い取られる固定時間割の案を、３秒くらいで考えてくれます。\nウリは、時間講師（〇曜日の午前中だけ、〇年〇組の授業を〇回担当する）も設定できることです。",
    thumbnail: "images/timetable_gene.png",
    download: "https://github.com/a071013n-sudo/my-tool/releases/download/timetable_gene/timetable_gene.html",
    repo: "https://github.com/a071013n-sudo/my-tool",
    safety: SAFETY_HTML
  },
  {
    id: "club_assign",
    icon: "🏸",
    name: "クラブ希望調査調整ツール",
    category: "校務・事務",
    env: "ブラウザのみ",
    tags: ["インストール不要", "校務PCで使える", "HTMLファイル"],
    summary: "年度末に大変なクラブ希望調査の調整が3秒ほどで終わります。Formsで調査を取ると更に楽です。",
    description: "担当になってしまうと年度末すっごい大変なクラブの希望調査の調整が、３秒くらいで終わります。\nFormsなどで希望調査を取ると、更に楽です。",
    thumbnail: "images/club_assign.png",
    download: "https://github.com/a071013n-sudo/my-tool/releases/download/club_assign/club-assign.html",
    repo: "https://github.com/a071013n-sudo/my-tool",
    safety: SAFETY_HTML
  },
  {
    id: "QRcode-maker",
    icon: "🔳",
    name: "オフラインQRコード作成",
    category: "校務・事務",
    env: "ブラウザのみ",
    tags: ["インストール不要", "校務PCで使える", "HTMLファイル"],
    summary: "校務PCに届いてしまったURLをQRコードにできます。ネットが使える端末のカメラで読み取れます。",
    description: "校務PCに送られてきてしまったURLをQRコードにできます。\nネットが使える端末のカメラで読み取れるようになります。",
    thumbnail: "images/QRcodemaker.png",
    download: "https://github.com/a071013n-sudo/my-tool/releases/download/%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E4%B8%8D%E8%A6%81/QRcodemaker.html",
    repo: "https://github.com/a071013n-sudo/my-tool",
    safety: SAFETY_HTML
  },
  {
    id: "hyoki_kensaku",
    icon: "🔎",
    name: "表記便覧　検索ソフト",
    category: "文書・表記",
    env: "ブラウザのみ",
    tags: ["インストール不要", "校務PCで使える", "HTMLファイル"],
    summary: "表記便覧をパラパラめくらなくてよくなります。",
    description: "表記便覧をパラパラめくらなくてよくなります。",
    thumbnail: "images/hyoki_kensaku.png",
    download: "https://github.com/a071013n-sudo/my-tool/releases/download/%E8%A1%A8%E8%A8%98%E4%BE%BF%E8%A6%A7/kyoki_kensaku.html",
    repo: "https://github.com/a071013n-sudo/my-tool",
    safety: SAFETY_HTML
  },
  {
    id: "hyoki_syusei",
    icon: "✏️",
    name: "表記便覧に合わせてExcelやWordを自動で修正",
    category: "文書・表記",
    env: "ブラウザのみ",
    tags: ["インストール不要", "校務PCで使える", "所見の表記統一"],
    summary: "所見などのExcel・Wordの表記を、表記便覧に合わせて自動で直します。組織で表記を統一できます。",
    description: "よく考えたら所見はみなさんExcelで書いていたことに気付いたので、自動で修正できるものを作成しました。\nこのファイル上でのみ動作するので、情報は外部に漏れません。\n組織で簡単に表記を統一できます。",
    thumbnail: "images/hyoki_syusei.png",
    download: "https://github.com/a071013n-sudo/my-tool/releases/download/1/hyoki_syusei.html",
    repo: "https://github.com/a071013n-sudo/my-tool",
    safety: SAFETY_HTML
  },
  {
    id: "pic_compress",
    icon: "🖼️",
    name: "画像圧縮ソフト",
    category: "ファイル整理",
    env: "Windows",
    tags: ["インストール不要", "校務PCで使える", "実行ファイル"],
    summary: "共有フォルダが真っ赤なときに。1MB以上の画像を500KB程度まで圧縮します。",
    description: "「共有フォルダがもういっぱいで、真っ赤！」ってときに使ってください。\n1MB以上の画像ファイルを500KB程度まで圧縮します。\n圧縮し過ぎを防ぐために、1MB以下のファイルは処理をスキップします。",
    thumbnail: "images/pic_compress.png",
    download: "https://github.com/a071013n-sudo/my-tool/releases/download/pic_compress/pic_compress.exe",
    repo: "https://github.com/a071013n-sudo/my-tool",
    safety: SAFETY_EXE
  },
  {
    id: "mov_compress",
    icon: "🎬",
    name: "動画圧縮ソフト",
    category: "ファイル整理",
    env: "Windows",
    tags: ["インストール不要", "校務PCで使える", "実行ファイル"],
    summary: "行事の記録ビデオが大きすぎる問題を解決。PC画面で見る分に支障のないサイズまで圧縮します。",
    description: "行事の記録ビデオサイズ大きすぎる問題を解決できます。\n「共有フォルダがもういっぱいで、真っ赤！」ってときにも使ってください。\n動画ファイルをPC画面で見る分には支障ないサイズまで圧縮します。",
    thumbnail: "images/mov_compress.png",
    download: "https://github.com/a071013n-sudo/my-tool/releases/download/mov_compress/mov_compress.exe",
    repo: "https://github.com/a071013n-sudo/my-tool",
    safety: SAFETY_EXE
  },
  {
    id: "gakugeikai_index",
    icon: "🎭",
    name: "学芸会の脚本インデックス",
    category: "行事",
    env: "Windows",
    tags: ["インストール不要", "実行ファイル"],
    summary: "探すのが大変な、学芸会に使っていい脚本のインデックス。ここから生成AIと脚本を考えると楽です。",
    description: "意外と探すのが大変な、学芸会に使っていい脚本のインデックス。\nここから生成AIと脚本を考えると楽です。",
    thumbnail: "images/gakugeikai_index.png",
    download: "https://github.com/a071013n-sudo/my-tool/releases/download/gakugeikai_index/gakugeikai_index.exe",
    repo: "https://github.com/a071013n-sudo/my-tool",
    safety: SAFETY_EXE
  },
  {
    id: "waveform_editor",
    icon: "🎵",
    name: "音楽データ波形編集ソフト",
    category: "行事",
    env: "Windows",
    tags: ["インストール不要", "校務PCで使える", "実行ファイル"],
    summary: "運動会や学芸会の音響編集に必要な機能だけに絞りました。MP3で出力します。",
    description: "運動会や学芸会の音響編集に必要な機能だけにしました。\nMP3で出力をします。",
    thumbnail: "images/waveform_editor.png",
    download: "https://github.com/a071013n-sudo/my-tool/releases/download/waveform_editor/waveform_editor.exe",
    repo: "https://github.com/a071013n-sudo/my-tool",
    safety: SAFETY_EXE
  }
];
