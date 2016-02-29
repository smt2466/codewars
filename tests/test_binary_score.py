# coding=utf-8
# pylint: disable=missing-docstring

"""
Binary scORe
"""

from src.binary_score import score


def test_zero():
    assert score(0) == 0


def test_one():
    assert score(1) == 1


def test_multi_digit():
    assert score(49) == 63


def test_big_number():
    assert score(1000000) == 1048575
