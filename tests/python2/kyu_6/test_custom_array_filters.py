# pylint: disable=missing-docstring, redefined-builtin

"""Custom Array Filters"""

import pytest

from python2.kyu_6.custom_array_filters import list


@pytest.fixture
def array():
    return [1, 2, 3, 4, 5]


def test_even_filter(array):
    assert list(array).even() == [2, 4]


def test_odd_filter(array):
    assert list(array).odd() == [1, 3, 5]


def test_under_filter(array):
    assert list(array).under(4) == [1, 2, 3]


def test_over_filter(array):
    assert list(array).over(4) == [5]


def test_in_range_filter(array):
    assert list(array).in_range(1, 3) == [1, 2, 3]


def test_filters_work_together():
    assert list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).even().under(5) == [2, 4]


def test_only_integers_allowed():
    assert list(["a", 1, 300, 63, 122, 181, 0.83]).even() == [300, 122]
