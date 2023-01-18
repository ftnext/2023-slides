"""VS CodeのRename Symbol機能でリファクタリングする

https://code.visualstudio.com/docs/editor/refactoring#_rename-symbol

- 「変数名の変更」 https://refactoring.com/catalog/renameVariable.html
- 「関数名の変更」 https://refactoring.com/catalog/changeFunctionDeclaration.html
"""

height = 50
width = 100
# [rename variable]
# 面積の計算。a を area にrenameする
a = height * width
# [rename variable]
print(a)


# [rename variable & rename function]
# 面積を計算する関数。calc を calc_area にrenameする
def calc(height, weight):
    # スコープを考慮してrenameされる例
    a = height * weight
    return a
    # [rename variable & rename function]
    # 変数aを使っているのは説明のため。(IMO) aを使わない実装のほうが分かりやすいと考えます
    # return height * weight


print(calc(50, 100))
