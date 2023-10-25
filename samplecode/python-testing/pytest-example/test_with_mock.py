from unittest.mock import patch


def a_func():
    ...


def b_func():
    ...


def c_func():
    ...


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
