:ogp_title: taskipyを使ったPython開発環境の一例
:ogp_event_name: stapy-june
:ogp_slide_name: development-environment-with-taskipy
:ogp_description: 2023/06 みんなのPython勉強会#94 LT
:ogp_image_name: stapy-june-taskipy

============================================================
taskipyを使ったPython開発環境の一例
============================================================

:Event: みんなのPython勉強会#94 LT
:Presented: 2023/06/15 nikkie

お前、誰よ
============================================================

* **にっきー** ／ :fab:`twitter` `@ftnext <https://twitter.com/ftnext>`__ ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ 
* みんなのPython勉強会 4代目LT王子・スタッフ
* 株式会社ユーザベースのデータサイエンティスト（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）

オーダー、鬼滅ネタ
--------------------------------------------------

.. raw:: html

    <blockquote class="twitter-tweet" data-align="center" data-dnt="true"><p lang="ja" dir="ltr">鬼滅ネタ、いいね！今度LTしちゃう？</p>&mdash; Takeshi Akutsu (@akucchan_world) <a href="https://twitter.com/akucchan_world/status/1666449005797097477?ref_src=twsrc%5Etfw">June 7, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

taskipyを使った **Python開発環境** の一例
============================================================

Python環境構築には **流派** がある
--------------------------------------------------

* Python使い＝〇〇したくてPythonを使う＝ *鬼と闘う* （鬼殺隊の一員）
* Python開発環境構築はさまざま＝ *呼吸はさまざま* （霞、恋）

  * 今日のトークからも（Python本家、Anaconda）

最近のnikkie： **pyenv + venv** の呼吸
--------------------------------------------------

* `pyenv <https://github.com/pyenv/pyenv>`__ でPythonのバージョンを管理
* venv（仮想環境）でプロジェクトごとの依存ライブラリを管理
* `Poetry <https://python-poetry.org/docs/>`__ の呼吸に憧れている（他には `rye <https://github.com/mitsuhiko/rye>`__ の呼吸）

IMO：紹介した方法を絶対採用、ではないです
--------------------------------------------------

* Pythonを使うという共通点がある
* **好みはそれぞれ**、文脈も各の持ち場で異なる
* オススメしますが、食指が動かなければ不採用でも全然OK🙆‍♂️

📌 **pyenv + venv の呼吸 弐の型 taskipy**
============================================================

本LTでの主張

taskipyを使った **Python開発** 環境の一例
============================================================

先人の知恵： **ツール** を使って開発しやすく✨
--------------------------------------------------

* PyCon JP 2019 `Python開発を円滑に進めるためのツール設定 <https://pycon.jp/2019/schedule/?sessionId=151>`__
* PyCon JP 2020 `チーム開発立ち上げにやっておいたほうがいいソース管理の方法 <https://pycon.jp/2020/timetable/?id=203858>`__
* PyCon Kyushu 2022 `静的コード解析から見出す一人前Pythonistaへの道 <https://www.docswell.com/s/moonwalkerpoday/ZP4VE5-2022-01-22-133417>`__

スタイルガイド PEP 8
--------------------------------------------------

* （守らなくてもコードは動くけど）「Pythonをこういうふうに書きましょう」
* https://peps.python.org/pep-0008/
* 人が頑張る道もあるけど、 **ツールを使ってPEP 8に沿う**

開発しやすくするツールの例
--------------------------------------------------

* Black：Pythonコードを自動に **整える**
* Flake8：Pythonコードの **静的解析**

最初の一歩『`Python実践レシピ <https://gihyo.jp/book/2022/978-4-297-12576-9>`__』2章

Black
--------------------------------------------------

* スタイルガイドに合うコードに **有無を言わさず整形**
* https://black.readthedocs.io/en/stable/

.. code-block:: shell

    % pip install black
    % # conda install -c conda-forge black

.. https://anaconda.org/conda-forge/black

.. revealjs-break::

.. literalinclude:: example.py
    :language: python
    :caption: example.py

:command:`black -l 79 example.py`

.. code-block:: diff

    -print ( 'hello, world' )
    +print("hello, world")

Flake8
--------------------------------------------------

* コードを実行せずに（＝静的）解析して、**スタイルや問題を指摘**
* https://flake8.pycqa.org/en/stable/

.. code-block:: shell

    % pip install flake8
    % # conda install -c anaconda flake8

.. https://anaconda.org/anaconda/flake8

.. revealjs-break::

:command:`flake8 example.py`

.. code-block:: txt

    example.py:1:1: F401 'calendar' imported but unused
    example.py:3:6: E211 whitespace before '('
    example.py:3:8: E201 whitespace after '('
    example.py:3:23: E202 whitespace before ')'

nikkieは思った「コマンドをまとめたい」
--------------------------------------------------

* :command:`black` の後に :command:`flake8` だとスタイル関係は指摘されない（この順にしたい）
* ほかにも :command:`pytest` などなどたくさんのツール。便利だけど、覚えていられない🤯（実行漏れもある）
* *順番も含めて、1つのコマンドにまとめられないかな？*

**taskipy** を使ったPython開発環境の一例
============================================================

taskipy
--------------------------------------------------

* Python向けの **タスクランナー**
* https://github.com/taskipy/taskipy/
* 書きました「`Python向けタスクランナーとして気になっていたtaskipy 素振りの記、Poetryのない環境でお試し <https://nikkie-ftnext.hatenablog.com/entry/start-taskipy-without-poetry>`__」

taskipy インストール
--------------------------------------------------

.. code-block:: shell

    % pip install taskipy

* https://pypi.org/project/taskipy/
* :command:`conda` コマンドでインストールできるかは未確認です🙏

:file:`pyproject.toml` を書く
--------------------------------------------------

.. code-block:: toml

    [tool.taskipy.tasks]
    format = "black -l 79 awesome_lib tests"
    test = "pytest"
    check = "flake8 awesome_lib tests"

:command:`task` コマンド
--------------------------------------------------

.. code-block:: shell

    % task format  # blackを使ったフォーマット
    % task test  # pytestで単体テスト実行
    % task check  # flake8を使った静的解析

コマンドのオプションを覚えておく必要、なくなった🙌

taskipyの **フック** ✨
--------------------------------------------------

* ``pre_test`` は ``test`` の **前** に実行するタスクになる
* ``post_test`` で ``test`` の **後** に実行するタスクになる
* ``format`` や ``check`` を設定すると...

:command:`task test` ですべて流れる！
--------------------------------------------------

.. code-block:: toml
    :emphasize-lines: 3,5,6

    [tool.taskipy.tasks]
    format = "black -l 79 awesome_lib tests"
    test = "pytest"
    check = "flake8 awesome_lib tests"
    pre_test = "task format"
    post_test = "task check"

フォーマット➡️テスト➡️静的解析が **1コマンド** に！

実際のプロジェクトでの設定例
--------------------------------------------------

* **もっとたくさんのツール** をまとめています
* https://github.com/ftnext/the-solitary-castle-in-the-mirror-cli/blob/a91d99167760af2213eda0f4867b7f63b97aad66/pyproject.toml#L23-L34
* 書きました「`Python開発環境共有、今の私はtaskipyで一連のコマンドをつないでいます <https://nikkie-ftnext.hatenablog.com/entry/python-development-environment-taskipy-example-202306>`__」

まとめ🌯 taskipyを使ったPython開発環境の一例
============================================================

* pyenv + venv の呼吸 弐の型 taskipy
* Pythonでの開発、ツールを使ってやりやすくできる
* **多様なツールをtaskipyでまとめ** たらいい感じ（フック素晴らしい！）

ご清聴ありがとうございました
--------------------------------------------------

Enjoy Python!

Appendix
============================================================

* オススメ `もうPythonの細かい書き方で議論しない。blackで自動フォーマットしよう <https://blog.hirokiky.org/entry/2019/06/03/202745>`__
* Flake8は今後Ruffに変わるかも？ `新しい静的コード解析ツール「Ruff」をご紹介 <https://gihyo.jp/article/2023/03/monthly-python-2303>`__

EOF
===
