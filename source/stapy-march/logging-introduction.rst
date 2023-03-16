:ogp_title: Pythonのlogging入門
:ogp_event_name: stapy-march
:ogp_slide_name: logging-introduction
:ogp_description: 2023/03 みんなのPython勉強会#91 10分トーク2本立て 2/2
:ogp_image_name: stapy-march-logging

============================================================
Pythonのlogging入門
============================================================

:Event: みんなのPython勉強会#91
:Presented: 2023/03/16 nikkie

お前、誰よ（知ってる）
============================================================

* **にっきー** ／ `はてなブログ <https://nikkie-ftnext.hatenablog.com/>`__ （毎日1記事書いてます） 
* みんなのPython勉強会 4代目LT王子 スタッフ
* PyCon JP 2021 座長
* `SpeechRecognition <https://github.com/Uberi/speech_recognition>`__ メンテナ

Pythonのlogging入門
============================================================

* 2本立ての2本目です。引き続きChatGPTとお楽しみいただいても全然大丈夫
* loggingモジュールに苦手意識がありましたが、 **理解が進んだポイントを共有** します
* 「なぜログが必要か」は今回は話しません

もっとも単純な例
============================================================

.. doctestを通すために標準出力を指定する（ここが唯一有効なbasicConfig）
    >>> import logging, sys
    >>> logging.basicConfig(stream=sys.stdout)

.. code-block:: python

    >>> import logging
    >>> logging.warning('Watch out!')
    WARNING:root:Watch out!

https://docs.python.org/ja/3/library/logging.html

``logging.warning``
--------------------------------------------------

    レベル WARNING のメッセージをルートロガーで記録します。

https://docs.python.org/ja/3/library/logging.html#logging.warning

もっとも単純な例で完全に理解😎
--------------------------------------------------

* WARNING以外のレベルのメッセージも記録してみよう
* `ロギングレベル <https://docs.python.org/ja/3/library/logging.html#logging-levels>`_ を参照

  * `logging を使うとき <https://docs.python.org/ja/3/howto/logging.html#when-to-use-logging>`__ の「レベル」もいいぞ

レベル ERROR
--------------------------------------------------

.. code-block:: python

    >>> logging.error('ヤバイよ。マジヤバイよ')
    ERROR:root:ヤバイよ。マジヤバイよ

https://docs.python.org/ja/3/library/logging.html#logging.error

レベル INFO、あれ？😳
--------------------------------------------------

.. code-block:: python

    >>> logging.info('想定通り')

https://docs.python.org/ja/3/library/logging.html#logging.info

1️⃣ロガーとロギングレベル
============================================================

* なぜレベル INFOのメッセージは画面に出力されなかったのでしょう？

``logging.warning`` はロガーを設定
--------------------------------------------------

* ロガー＝ ``logging.Logger`` クラスのインスタンス
* ``logging.warning`` が設定するのは *ルート* ロガー

ルートロガー
--------------------------------------------------

.. code-block:: python

    >>> # ルートロガーを取得
    >>> root_logger = logging.getLogger()
    >>> root_logger  # (WARNING) に注目
    <RootLogger root (WARNING)>

なぜレベル INFOのメッセージは出力されなかった？
--------------------------------------------------

    デフォルトのレベルは WARNING なので、INFO メッセージは現れません。

https://docs.python.org/ja/3/howto/logging.html#a-simple-example

高いレベル・低いレベルがある
--------------------------------------------------

* (高) ERROR
* WARNING
* (低) INFO

`ロギングレベル`_

ロギングレベルを設定する
--------------------------------------------------

* ルートロガーのロギングレベルは ``logging.basicConfig`` で指定できる
* https://docs.python.org/ja/3/library/logging.html#logging.basicConfig

ロギングレベルをINFOに指定（対話モード立ち上げ直し）
-----------------------------------------------------------

.. basicConfigは一度だけ有効なので、doctestを通すために裏で設定する
    >>> logging.getLogger().setLevel(logging.INFO)

.. code-block:: python

    >>> import logging
    >>> logging.basicConfig(level=logging.INFO)
    >>> logging.getLogger()  # (INFO) になってます！
    <RootLogger root (INFO)>
    >>> logging.info('想定通り')
    INFO:root:想定通り

🥟ロガーとロギングレベル
--------------------------------------------------

* ルートロガーはレベルがWARNING
* ルートロガーのレベルより下のレベルのINFOやDEBUGのメッセージは出力されない
* ``logging.basicConfig(level=...)`` で **ルートロガーのレベルを変えられる**

2️⃣ログメッセージの書式
============================================================

* なぜ「WARNING:root:Watch out!」という書式なのでしょう？

``logging.info`` や ``logging.warning`` の秘密
------------------------------------------------------------

    ルートロガーにハンドラが接続されていない場合、この関数 (および info(), warning(), error() そして critical()) は basicConfig() を呼び出します。

https://docs.python.org/ja/3/library/logging.html#logging.debug

``logging.basicConfig()`` が呼び出されていた！
------------------------------------------------------------

* **引数無し** での呼び出し
* 書式に関わるのは ``format`` 引数（`ドキュメント <https://docs.python.org/ja/3/library/logging.html#logging.basicConfig>`__）

    デフォルトは levelname, name, message 属性をコロン区切りにしたものです。

デフォルトのログメッセージの書式
------------------------------------------------------------

* 「WARNING:root:Watch out!」
* **レベル:ロガーの名前:メッセージ**
* ``"%(levelname)s:%(name)s:%(message)s"``

書式を変えてみよう（対話モード立ち上げ直し）
--------------------------------------------------

.. basicConfigは一度だけ有効なので、doctestを通すために裏で設定する
    >>> logging.getLogger().setLevel(logging.INFO)

.. code-block:: python

    >>> import logging
    >>> log_format = "%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
    >>> logging.basicConfig(level=logging.INFO, format=log_format)
    >>> logging.info('想定通り')  # doctest: +SKIP
    2023-03-15 21:03:40,253 | INFO | root:<module>:1 - 想定通り

書式の指定
--------------------------------------------------

* ドキュメントの `LogRecord 属性 <https://docs.python.org/ja/3/library/logging.html#logrecord-attributes>`_ 参照
* `%(asctime)s`: LogRecord が生成された時刻を人間が読める書式で表したもの
* `%(funcName)s`: ロギングの呼び出しを含む関数の名前

🥟ログメッセージの書式
--------------------------------------------------

* ``logging.basicConfig(format=...)`` で **ログメッセージの書式を変えられる**
* ログメッセージの書式はドキュメントの `LogRecord 属性`_ に一覧あり

3️⃣ログの出力先
============================================================

* 画面以外にも出力するには？（ファイル）
* *ハンドラ* が関わります

ルートロガーのハンドラ（対話モード立ち上げ直し）
--------------------------------------------------

.. code-block:: python

    >>> import logging
    >>> logging.warning('Watch out!')
    WARNING:root:Watch out!
    >>> logging.getLogger().handlers  # doctest: +SKIP
    [<StreamHandler <stderr> (NOTSET)>]

ハンドラとは
--------------------------------------------------

    ハンドラは、(ロガーによって生成された) ログ記録を適切な送信先に送ります。

https://docs.python.org/ja/3/library/logging.html#logging.basicConfig

``logging.StreamHandler``
--------------------------------------------------

* ストリームにログを送るハンドラ
* https://docs.python.org/ja/3/library/logging.handlers.html#logging.StreamHandler
* ログは **標準エラー出力** に出力される

脱線：標準出力も指定可能（対話モード立ち上げ直し）
--------------------------------------------------

.. code-block:: python

    >>> import logging
    >>> import sys
    >>> logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    >>> logging.getLogger().handlers  # doctest: +SKIP
    [<StreamHandler <stdout> (NOTSET)>]    

ファイルにログ出力したい
--------------------------------------------------

* ``basicConfig`` の ``filename`` 引数を指定する

    StreamHandler ではなく指定された名前で FileHandler が作られます。

https://docs.python.org/ja/3/library/logging.html#logging.basicConfig

ファイルにログ出力したい
--------------------------------------------------

.. code-block:: python

    >>> import logging
    >>> logging.basicConfig(level=logging.INFO, filename="awesome.log")
    >>> logging.warning('Watch out!')  # doctest: +SKIP
    >>> logging.info('想定通り')  # doctest: +SKIP

.. code-block:: shell

    $ cat awesome.log
    WARNING:root:Watch out!
    INFO:root:想定通り

🥟ログの出力先
============================================================

* ``logging.basicConfig(filename=...)`` でファイルにログ出力できる
* ハンドラ ``StreamHandler`` や ``FileHandler``

🥟 ``basicConfig`` で **ルートロガーを設定** できる
============================================================

* ``level``: ロギングレベル
* ``format``: ログメッセージ書式
* ``filename``: FileHandler

``import logging; logging.info("想定通り")`` が出力されないのは
---------------------------------------------------------------------

* （ルートロガー未設定なので） ``logging.info`` は ``logging.basicConfig()`` を呼び出す
* ルートロガーがレベル **WARNING** で設定される
* WARNINGより低いINFOレベルは出力されない

深堀り ``logging.warning``
============================================================

    ルートロガーにハンドラが接続されていない場合、この関数 (および info(), warning(), error() そして critical()) は basicConfig() を呼び出します。

https://docs.python.org/ja/3/library/logging.html#logging.debug

``logging.basicConfig``
--------------------------------------------------

    デフォルトの Formatter を持つ StreamHandler を生成してルートロガーに追加し、ロギングシステムの基本的な環境設定を行います。

https://docs.python.org/ja/3/library/logging.html#logging.basicConfig

``logging.warning`` が呼び出した ``logging.basicConfig`` で
---------------------------------------------------------------------

* Formatterを生成
* StreamHandlerを生成
* これらを **ルートロガーに追加**

画面に「WARNING:root:Watch out!」と現れたのは
---------------------------------------------------------------------

* ルートロガーのロギングレベルは **WARNING**
* ``"%(levelname)s:%(name)s:%(message)s"`` **書式** のFormatter
* StreamHandlerは **標準エラー出力** に出力

ロガーの階層構造
============================================================

* ルートロガー以外のロガーについて
* ポイントは階層構造（**親子関係**）

ルートロガー以外のロガー
--------------------------------------------------

* ``logging.getLogger`` にロガーの名を渡せる

  * ``logging.getLogger("awesome")``

* モジュールレベルロガー ``logging.getLogger(__name__)``

ロガーの親子関係（階層構造）
--------------------------------------------------

* ``getLogger("foo.bar")``
* ``getLogger("foo")`` foo.barの親
* ``getLogger()`` ルートロガー、 **すべての親**

https://docs.python.org/ja/3/howto/logging.html#advanced-logging-tutorial

``propagate`` 属性
--------------------------------------------------

    この属性が真と評価された場合、このロガーに記録されたイベントは、このロガーに取り付けられた全てのハンドラに加え、上位 (祖先) ロガーのハンドラにも渡されます。 

https://docs.python.org/ja/3/library/logging.html#logging.Logger.propagate

``propagate`` 属性（承前）
--------------------------------------------------

    A.B.C という名前のロガーの propagate 属性が真と評価された場合、(略)

    最初に A.B.C に接続されたハンドラに渡され、その後 A.B, A という名前のロガー、そしてルートロガーという順番で各ロガーに接続されたハンドラに渡されます。

子のロガーから親のロガーに伝播する
--------------------------------------------------

* ``getLogger("foo.bar")`` で記録されるログは
* 親の ``getLogger("foo")`` にも伝播し
* すべての親 ルートロガー ``getLogger()`` にも伝播する

例 ``logging.warning`` したばっかりに
============================================================

* 奇妙な挙動ですが、 **階層構造** を押さえていると理解できると思います
* ``logging.warning`` は ``basicConfig`` で *ルートロガーにハンドラを設定*

``logging.warning`` したばっかりに
--------------------------------------------------

.. code-block:: python

    >>> import logging
    >>> logging.warning('Watch out!')
    WARNING:root:Watch out!

ルートロガーが設定された（フォーマッタとStreamHandler）

子ロガー用のフォーマッタ、ハンドラ設定
--------------------------------------------------

.. code-block:: python

    >>> log_format = "%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
    >>> formatter = logging.Formatter(log_format)
    >>> handler = logging.StreamHandler()
    >>> handler.setFormatter(formatter)

子ロガー ``practice`` の設定
--------------------------------------------------

.. code-block:: python

    >>> logger = logging.getLogger("practice")
    >>> logger.setLevel(logging.INFO)
    >>> logger.addHandler(handler)

レベルはINFO、StreamHandlerも設定

奇妙な挙動？ propagateによる
--------------------------------------------------

.. code-block:: python

    >>> logger.info('想定通り')  # doctest: +SKIP
    2023-03-15 22:21:43,880 | INFO | practice:<module>:1 - 想定通り
    INFO:practice:想定通り

**2行出力** されてしまう

ロガーの階層構造
--------------------------------------------------

* 日付で始まる行

  * 子ロガー（practice）による出力

* もう1行

  * 親の **ルートロガーによる出力**
  * 子ロガーが記録するINFOレベルが伝播した

参考：子ロガーにハンドラがなくても出力される！
--------------------------------------------------

.. code-block:: python

    >>> logger = logging.getLogger("practice")
    >>> logger.setLevel(logging.INFO)
    >>> # logger.addHandler(handler)
    >>> logger.info('想定通り')  # doctest: +SKIP
    INFO:practice:想定通り

ルートロガーに伝播して出力

``logging.warning`` がないだけで
--------------------------------------------------

.. code-block:: python

    >>> # logging.warning がない以外は共通のコード
    >>> logger.info('想定通り')  # doctest: +SKIP
    2023-03-15 22:27:32,375 | INFO | practice:<module>:1 - 想定通り

**子ロガー** に設定した **ハンドラ** による1行のみ出力

実体験に基づく例でした
--------------------------------------------------

* 子ロガーにFileHandlerを指定して、この体験を味わいました
* ルートロガーからStreamHandlerを *引き剥がす実装* が必要でした...
* 詳しくは https://nikkie-ftnext.hatenablog.com/entry/python-logging-root-logger-and-chain-propagation

IMO ライブラリ開発でのlogging利用
--------------------------------------------------

* ライブラリで ``logging.warning`` や ``logging.basicConfig`` は、利用者に苦労をかけるので望ましくないと考えます
* 自戒を込めて、`NullHandler <https://docs.python.org/ja/3/library/logging.handlers.html#logging.NullHandler>`__ を使っていきたい（教えてChatGPT🙏）

Logging クックブックより
--------------------------------------------------

    もしあなたがライブラリのメンテナンスをしているのであれば、 NullHandler インスタンス以外のロガーを追加してはいけない、ということを意味します。

https://docs.python.org/ja/3/howto/logging-cookbook.html#adding-handlers-other-than-nullhandler-to-a-logger-in-a-library

まとめ🌯 Pythonのlogging入門
============================================================

* もっとも単純な例 ``logging.warning`` は ``logging.basicConfig`` を **呼んでいた**

  * ルートロガーにStreamHandlerを設定

* ライブラリの中で ``logging.warning`` や ``logging.basicConfig`` はNG🙅‍♂️です

2本ご清聴ありがとうございました
--------------------------------------------------

Happy development!

References
============================================================

オススメのリソース
--------------------------------------------------

* 『`Python実践レシピ <https://gihyo.jp/book/2022/978-4-297-12576-9>`__』17.4 ログを出力する―logging
* PyCon JP 2021 `Loggingモジュールではじめるログ出力入門 <https://2021.pycon.jp/time-table?id=272259>`__

公式ドキュメント
--------------------------------------------------

* `Logging HOWTO <https://docs.python.org/ja/3/howto/logging.html>`__ （基本／上級チュートリアル）
* `Logging クックブック <https://docs.python.org/ja/3/howto/logging-cookbook.html>`__
* https://docs.python.org/ja/3/library/logging.html

nikkieのアウトプット
--------------------------------------------------

* `Pythonのloggingを よ う や く 完全に理解しました 〜revChatGPTでdebugレベルログを出そうとした試行錯誤を題材に〜 <https://nikkie-ftnext.hatenablog.com/entry/python-logging-root-logger-and-chain-propagation>`__
* `Pythonのloggingモジュールのドキュメントの「もっとも単純な例」を説明する 〜logging.warningの裏側で起こっていること〜 <https://nikkie-ftnext.hatenablog.com/entry/python-logging-the-simplest-example-under-the-hood>`__

EOF
===
