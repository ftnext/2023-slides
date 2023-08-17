============================================================
:file:`pyproject.toml` の一歩目
============================================================

:Event: みんなのPython勉強会#96 LT
:Presented: 2023/08/17 nikkie

お前、誰よ
============================================================

* **にっきー** ／ :fab:`twitter` `@ftnext <https://twitter.com/ftnext>`__ ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ 
* みんなのPython勉強会 4代目LT王子・スタッフ
* 株式会社ユーザベースのデータサイエンティスト（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）

このLTでは
============================================================

* まずPythonイベントのインフォメーションをお伝えします（コミュニティ盛り上がったらいいな〜）
* :file:`pyproject.toml` について話します

ℹ️インフォメーションℹ️
============================================================

本編：:file:`pyproject.toml` の一歩目
============================================================

ライブラリを自作したことある方？🙋‍♂️🙋‍♀️
============================================================

自作ライブラリの公開
--------------------------------------------------

* PyPI

.. code-block:: shell

    $ pip install kojo-fan-art

* GitHubからも :command:`pip install` できる

GitHubから :command:`pip install` の例
--------------------------------------------------

.. code-block:: shell

    $ pip install git+https://github.com/karaage0703/unko

からあげさん `Pythonで自分だけのクソライブラリを作る方法 <https://zenn.dev/karaage0703/articles/db8c663640c68b>`__

GitHubからインストールできる秘密
------------------------------------------------------------

.. code-block:: python
    :caption: setup.py

    from setuptools import setup, find_packages

    setup(
        name='unko',
        version='0.1',
        packages=find_packages()
    )

https://github.com/karaage0703/unko/blob/main/setup.py

主張： :file:`setup.py` に代えて :file:`pyproject.toml` がオススメ！
======================================================================

nikkieと :file:`pyproject.toml`
--------------------------------------------------

* また新しいこと覚えなきゃいけないのか...（乗り気でない）
* Pythonコミュニティ的には :file:`pyproject.toml` への移行が進んでる？（私、取り残されてる？）
* 使ってみたら、学習コスト思ってたほど高くなかったし **便利じゃん**！

:file:`pyproject.toml` を使った自作ライブラリの公開
------------------------------------------------------------

.. code-block:: shell

    $ pip install git+https://github.com/ftnext/unko

:file:`setup.py` の代わりに :file:`pyproject.toml`
--------------------------------------------------

.. code-block:: toml

    [project]
    name = "unko"
    version = "0.1"

https://github.com/ftnext/unko/blob/main/pyproject.toml

:file:`pyproject.toml` は後発な分、わかりやすい！
--------------------------------------------------

.. code-block:: toml

    [project]
    dependencies = [
        "httpx",
    ]

:file:`setup.py` では ``install_requires``

:file:`pyproject.toml` は後発な分、わかりやすい！
--------------------------------------------------

.. code-block:: toml

    [project.optional-dependencies]
    dev = [
        "pytest",
    ]

:file:`setup.py` では ``extras_require`` （``install_requires`` と混乱しがちでした😵）

:file:`pyproject.toml` は **ツールの設定も** できる！
============================================================

インストールできるようにするだけじゃない！

Python開発に使う各種ツール
--------------------------------------------------

* Black（フォーマッタ）
* pytest（テストコード実行）
* mypy（型チェック）
* etc.etc.

:file:`pyproject.toml` でツールを設定！
--------------------------------------------------

* Gunosyさん `その設定、pyproject.tomlに全部書けます <https://data.gunosy.io/entry/linter_option_on_pyproject>`__
* nikkieは **taskipy** を使ってます。6月LT `taskipyを使ったPython開発環境の一例 <https://ftnext.github.io/2023-slides/stapy-june/development-environment-with-taskipy.html>`__

まとめ🌯 :file:`pyproject.toml` の一歩目
============================================================

* :file:`pyproject.toml` 便利なので、みんな使おう！
* **自作ライブラリ** を公開するときは :file:`setup.py` に代えて使ってみては（分かりやすい！）
* **ツールの設定を書く** 用途で導入もできます

ご清聴ありがとうございました
--------------------------------------------------

Enjoy Python with :file:`pyproject.toml`!

Appendix
============================================================

* `Pythonで自作ライブラリを作るとき、setup.pyに代えてpyproject.tomlを使ってみませんか？ <https://nikkie-ftnext.hatenablog.com/entry/why-dont-you-write-pyproject-toml-instead-of-setup-py>`__
* `使ってみようpyproject.toml！ projectの設定に使う項目のみんなを紹介するぜ！！ <https://nikkie-ftnext.hatenablog.com/entry/pyproject-toml-project-keys-and-examples>`__

EOF
===
