# coding=utf-8
# pylint: disable=invalid-name,missing-docstring,redefined-outer-name

""""
Zip it!
"""

import pytest

from src.python2.kyu_7.zip_it import lstzip


@pytest.fixture
def a():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def b():
    return ['a', 'b', 'c', 'd', 'e']


@pytest.fixture()
def concat():
    return lambda a, b: str(a) + str(b)


def test_simple_concatenation(a, b, concat):
    assert lstzip(a, b, concat) == ["1a", "2b", "3c", "4d", "5e"]


def test_reverse_concatenation(a, b):
    def func(b, a):
        return str(a) + str(b)
    assert lstzip(a, b, func) == ["a1", "b2", "c3", "d4", "e5"]


def test_nested_function(a, b, concat):
    def func(a, b):
        return a * ord(b[0])
    answer = ["a97", "b196", "c297", "d400", "e505"]
    assert lstzip(b, lstzip(a, b, func), concat) == answer


def test_short_b(a, b, concat):
    assert lstzip(a, b[:3], concat) == ["1a", "2b", "3c"]


def test_short_a(a, b, concat):
    assert lstzip(a[:3], b, concat) == ["1a", "2b", "3c"]
