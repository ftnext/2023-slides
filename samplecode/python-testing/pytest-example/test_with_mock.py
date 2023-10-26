import random
from unittest.mock import patch


def a_func(number: int):
    print(number)


def b_func(foo: str, bar: str):
    print(foo, bar)


def c_func():
    print(random.randint(1, 6))


def foo():
    a_func(42)
    b_func("ham", "egg")
    c_func()


@patch("test_with_mock.c_func")
@patch("test_with_mock.b_func")
@patch("test_with_mock.a_func")
def test_foo(a_func, b_func, c_func):
    foo()

    a_func.assert_called_once_with(42)
    b_func.assert_called_once_with("ham", "egg")
    c_func.assert_called_once_with()


if __name__ == "__main__":
    foo()
