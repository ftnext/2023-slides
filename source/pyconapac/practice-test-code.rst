======================================================================
好きとか嫌いとかはいい、練習してテストを書けるようになるんだ
======================================================================

好きとか嫌いとかはいい、 **練習してテストを書けるよ** うになるんだ
======================================================================

日本語資料・ **English talk** です

:Event: PyCon APAC 2023
:Presented: 2023/10/27 nikkie

.. The title is "Like It or Not, Practice Until You Can Write Tests".
    Thank you for choosing this talk. Enjoy it!

.. アニメのスラングすぎて、英語で伝えるのが難しい
    15分話していきます

お前、誰よ
============================================================

* nikkie（にっきー） ／ :fab:`twitter` `@ftnext <https://twitter.com/ftnext>`__ ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__
* 株式会社ユーザベースのデータサイエンティスト（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）

.. image:: https://drive.google.com/uc?id=19PMMnkqDiFMCJBPwoA1B51ltQBG0y4kL

.. Please call me nikkie.
    I usually write Python as a data scientist at a company "Uzabase".

.. にっきーと申します。
    ふだんはユーザベースという会社でデータサイエンティストとしてPythonを書いています

お前、誰よ 続）Pythonとアニメが好き
--------------------------------------------------

    | いまはまだできなくても大丈夫。
    | **これからできるようになればいい**

最近ハマってる #ミリアニネタバレ感想

.. (Continuing with self-introduction,) I love Python and anime.
    Here's a quote from a show I've recently become engrossed in:
    "It's okay if you can't do it now.
    With practice, you'll be able to in the future"
    Now, let's dive into the main topic.

.. 自己紹介の続きですが、Pythonとアニメが好きです。
    最近ハマっている作品の一節なのですが、
    いまはまだできなくても大丈夫。
    これからできるようになればいい。
    本編に入っていきましょう

.. https://twitter.com/ftnext/status/1715665132804841707

練習してテストを書けるようになるんだ
============================================================

* 前提：Pythonの **関数** が書ける
* いまはまだテストコードを書いたことがなくて大丈夫

.. This talk is intended for those of you who can write Python functions.
    Don't worry if you've never written test code before!
    Let's practice and get to the point where we can write tests.

.. このトークはPythonの関数が書ける方に聞いていただけたらいいなと思っています。
    いまはまだテストコードを書いたことがなくて大丈夫です！
    練習してテストを書けるようになっていきましょう

お品書き（兼 持ち帰れるもの）
--------------------------------------------------

1. テストコードが書けるメリット
2. doctestの使い方
3. pytestの使い方

.. I'm planning to cover three main points.
    First, I'll discuss the benefits of writing test code.
    After that, I'll show you two methods to write test codes.

.. 大きく3つのことを話そうと思っています。
    まずテストコードが書けるとこんないいことがあるよという話をします。
    その後テストコードをどう書くのかに対して、2つのやり方を示します。

動作環境 & サンプルコード
--------------------------------------------------

* Python 3.12.0 (latest🙌)
* :fab:`github` `doctest-example <https://github.com/ftnext/2023-slides/tree/main/samplecode/python-testing/doctest-example>`__
* :fab:`github` `pytest-example <https://github.com/ftnext/2023-slides/tree/main/samplecode/python-testing/pytest-example>`__

.. Sample codes work at Python 3.12.0!

.. コマンド控え
    python -m doctest fizzbuzz.py example_repr.py
    pytest --doctest-modules -v
    python -m doctest ../../../source/pyconapac/doctest.rst.txt ../../../source/pyconapac/pytest.rst.txt

.. include:: test-code-benefits.rst.txt

お品書き
--------------------------------------------------

1. テストコードが書けるメリット
2. **doctestの使い方**
3. pytestの使い方

テストコードをどう書くか Part 1/2

.. I'll introduce two methods to write tests.
    This is the first part of our discussion on how to write test code.
    🙋‍♂️ Has anyone here heard of the term "doctest"?

.. ここまでをもとにテストを書いてみたい方に、テストの書き方を2つ紹介します。
    テストコードをどう書くかという話の前半です。
    🙋‍♂️doctestという名称を聞いたことがある方？

.. include:: doctest.rst.txt

閑話休題🍵 お前、誰よ 続
============================================================

関わっているコミュニティの **ポスター** @20F

* Start Python Club (#stapy)
* 読書py

.. This is a slide for a break.（給水）
    I hope to see you at the poster session on the 20th floor!

.. breakのスライドです（給水する）
    20Fのポスターセッションでもお会いしましょう！

お品書き
--------------------------------------------------

1. テストコードが書けるメリット
2. doctestの使い方
3. **pytestの使い方**

テストコードをどう書くか Part 2/2

.. This is the final part.
    I will introduce another method called pytest.
    🙋‍♂️ Is anyone familiar with the name "pytest"?

.. 最後のパートです。
    テストコードをどう書くかに対して、pytestという別のやり方を紹介していきます。
    🙋‍♂️pytestという名称を聞いたことがある方？

.. include:: pytest.rst.txt

まとめ🌯 練習してテストを書けるようになるんだ
============================================================

* テストを書くと、動作する？ 間違えてない？という不安は **退屈** に変わる
* 関数の呼び出しと返り値を **docstringに書くだけ** で、doctestでテストできる！（一歩目）
* （拡張された）assert文をはじめ、 **テストコードが書きやすいpytest** もぜひ！

.. To summarize:
    Writing tests transforms the fear of "Is it working? Did I make a mistake?" into boredom.
    I've introduced two methods:
    The first, doctest, involves simply writing the function call and its return value in the docstring.
    The second is pytest, which makes writing test code easier.
    I encourage you to try out both of these approaches.

.. まとめます。
   テストを書くと、動作する？ 間違えてない？という不安は **退屈** に変わる
   やり方を2つ紹介しました。
   関数の呼び出しと返り値をdocstringに書くだけのdoctest、
   もう1個がテストコードが書きやすくなるpytest。
   これらをぜひ使ってみてください。

pytestはまだまだ序の口🏃‍♂️ (skip)
--------------------------------------------------

* パラメタ化テストを紹介
* *フィクスチャ*
* 『`テスト駆動Python <https://www.shoeisha.co.jp/book/detail/9784798177458>`__』

ご清聴ありがとうございました
--------------------------------------------------

好きとか嫌いとかはいい、練習してテストを書けるようになるんだ

Practice, practice, practice!!!

.. Thank you for your listening

References
============================================================

* 『`テスト駆動開発 <https://www.ohmsha.co.jp/book/9784274217883/>`__』（Kent Beck）

    テストは不安を退屈に変える賢者の石だ。（第25章）

* 『`ちょうぜつソフトウェア設計入門 <https://gihyo.jp/book/2022/978-4-297-13234-7>`__』（第6章）

.. include:: appendix.rst.txt

EOF
============================================================
