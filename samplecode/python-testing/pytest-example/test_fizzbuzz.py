import pytest

from fizzbuzz import fizzbuzz


def test_15の倍数のときはFizzBuzzを返す():
    assert fizzbuzz(15) == "FizzBuzz"


@pytest.mark.parametrize("number", [3, 6])
def test_3の倍数のときはFizzを返す(number):
    number = 3
    assert fizzbuzz(number) == "Fizz"


def test_5の倍数のときはBuzzを返す():
    assert fizzbuzz(5) == "Buzz"


def test_3の倍数でも5の倍数でもないときは文字列を返す():
    assert fizzbuzz(1) == "1"
