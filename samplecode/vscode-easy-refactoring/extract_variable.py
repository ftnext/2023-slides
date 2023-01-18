"""VS CodeのExtract variable機能でリファクタリングする

https://code.visualstudio.com/docs/python/editing#_extract-variable

- https://refactoring.com/catalog/extractVariable.html
"""


# [extract variable]
# base_price = order.quantity * order.item_price のように抽出する例
def price(order):
    # price = base price - quantity discount + shipping
    return (
        order.quantity * order.item_price
        - max(0, order.quantity - 500) * order.item_price * 0.05
        + min(order.quantity * order.item_price * 0.1, 100)
    )
# [extract variable]


from typing import NamedTuple


class Order(NamedTuple):
    quantity: int
    item_price: int


assert price(Order(quantity=600, item_price=100)) == 59600
