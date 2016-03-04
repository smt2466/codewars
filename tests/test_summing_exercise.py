# coding=utf-8
# pylint: disable=missing-docstring, redefined-outer-name, invalid-name

"""
Exercise in Summing
"""

import pytest

from src.summing_exercise import maximum_sum, minimum_sum


@pytest.fixture
def values():
    return [5, 4, 3, 2, 1]


def test_minimum_sum_returns_correct_result(values):
    assert minimum_sum(values, 2) == 3


def test_maximum_sum_returns_correct_result(values):
    assert maximum_sum(values, 3) == 12
