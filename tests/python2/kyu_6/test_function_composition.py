# pylint: disable=missing-docstring

"""Function Composition"""

from src.python2.kyu_6.function_composition import compose


def add1(num):
    return num + 1


def this(num):
    return num


def test_returns_correct_result():
    assert compose(add1, this)(0) == 1
