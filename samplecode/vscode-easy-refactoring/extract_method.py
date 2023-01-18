"""VS CodeのExtract method機能でリファクタリングする

https://code.visualstudio.com/docs/python/editing#_extract-method

- https://refactoring.com/catalog/extractFunction.html
"""


def print_banner():
    ...


def calculate_outstanding(invoice):
    ...


# [extract function]
# print detailsというコメントで説明された処理を関数に抽出する例
def print_owing(invoice):
    print_banner()
    outstanding = calculate_outstanding(invoice)

    # print details (<- 「関数を抽出」すると、このコメントは不要になる)
    print(f"name: {invoice.customer}")
    print(f"amount: {outstanding}")
# [extract function]
