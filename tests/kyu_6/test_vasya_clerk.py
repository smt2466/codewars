# pylint: disable=missing-docstring

"""Vasya - Clerk"""

from src.kyu_6.vasya_clerk import tickets


def test_returns_yes():
    assert tickets([25, 25, 50]) == 'YES'


def test_returns_no():
    assert tickets([25, 100]) == 'NO'
