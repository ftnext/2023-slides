:ogp_title: Awakening Extension (拡張開発はじまるよ🔰)
:ogp_event_name: vscodeconjp
:ogp_slide_name: awakening-extension
:ogp_description: 2023/01 VS Code Conference Japan 2022 - 2023 15分トークスライド
:ogp_image_name: vscodeconjp-extension

============================================================
Awakening Extension (拡張開発はじまるよ🔰)
============================================================

:Event: VS Code Conference Japan 2022 - 2023
:Presented: 2023/01/21 nikkie 14:35-

Thank you VSCodeConJP❤️
============================================================

* ㊗️ハイブリッド開催🎉
* 15分2本発表の機会をありがとうございます
* 2021開催がなければ、この発表は実現していません！

拡張開発はじまるよ🔰
============================================================

    | 過去のVS Code Conferenceのハンズオンテキストの内容を改造し、その拡張機能を公開するまでの
    | ありのまま（成功も失敗も両方）の記録である。

`イベントサイト <https://vscodejp.github.io/conference/2022-2023/ja/>`__ より

拡張開発の流れを追体験
--------------------------------------------------

* VS Code拡張開発の経験がない方（*過去の私* 含む）向け
* **開発〜公開までの流れ**・全体感を共有
* 「拡張開発やってみよう」と思っていただけたら🙌

お前、誰よ（知ってる）
============================================================

* わわわ、わたし、にっきー
* :fab:`twitter` `@ftnext <https://twitter.com/ftnext>`__ ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ ／ `はてなブログ <https://nikkie-ftnext.hatenablog.com/>`__
* Python大好き（**TypeScriptほぼ経験無し**）
* 株式会社ユーザベースでデータサイエンティスト（自然言語処理、XP）

突然の「VS Code拡張を作りたい！」
--------------------------------------------------

* それは2022年9月のこと
* 作るために必要な **情報には見当** がついていた
* 「うまくいけば作れるんじゃないか」と拡張開発に体当たり

自作した **TOKIMEKI editing**
--------------------------------------------------

https://marketplace.visualstudio.com/items?itemName=everlasting-diary.tokimeki-editing

砕けなかった🙌

環境情報
--------------------------------------------------

- VS Code 1.74.3
- Node.js v16.14.2
- npm 8.5.0

.. literalinclude:: ../../samplecode/awakening-extension/package.json
    :language: json
    :lines: 3-5

経験のない拡張開発の旅路
--------------------------------------------------

1. テキストをベースに写経 & 改造（メインパート）
2. 拡張のE2Eテストを書く
3. 拡張を公開

.. include:: extension/hands-on.rst.txt

.. include:: extension/e2e.rst.txt

.. include:: extension/publish.rst.txt

まとめ🌯：Awakening Extension (拡張開発はじまるよ🔰)
============================================================

1. テキストをベースに写経 & 改造
2. 拡張のE2Eテストを書く
3. 拡張を公開

テキストをベースに写経 & 改造
--------------------------------------------------

* **Yeoman** によるscaffold
* **CodeLens** で編集

  * 正規表現にマッチする箇所に作成
  * **コマンド** 呼び出し

拡張のE2Eテストを書く
--------------------------------------------------

フィクスチャのファイルに対して以下を検証

* CodeLensの **設定**
* CodeLensから実行される **コマンド** を直接実行した結果

拡張を公開
--------------------------------------------------

* **はじめは手動アップロード** がオススメ
* 慣れたら :command:`vsce` コマンドを

ご清聴ありがとうございました！
--------------------------------------------------

Enjoy extension! 🎀🌈

.. include:: extension/references.rst.txt

.. include:: extension/supplement.rst.txt

EOF
===
