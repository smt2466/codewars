# coding=utf-8
# pylint: disable=missing-docstring,redefined-outer-name

"""
Next Featured Number Higher than a Given Value
"""

import pytest

from python2.src.kyu_7.next_featured_number import next_numb


@pytest.fixture
def not_possible():
    return "There is no possible number that fulfills those requirements"


def test_even_number():
    assert next_numb(12) == 15


def test_odd_number():
    assert next_numb(13) == 15


def test_big_two_digit_number():
    assert next_numb(99) == 105


def test_big_number():
    assert next_numb(999999) == 1023459


def test_too_big_number(not_possible):
    assert next_numb(9999999999) == not_possible
