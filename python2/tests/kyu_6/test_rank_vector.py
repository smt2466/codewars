# coding=utf-8
# pylint: disable=missing-docstring

""""
Rank Vector
"""

from python2.src.kyu_6.rank_vector import ranks


def test_empty_rank():
    assert ranks([]) == []


def test_one_score():
    assert ranks([2]) == [1]


def test_two_same_scores():
    assert ranks([2, 2]) == [1, 1]


def test_different_scores():
    assert ranks([9, 3, 6, 19]) == [2, 4, 3, 1]


def test_different_and_same_scores():
    assert ranks([3, 3, 3, 3, 3, 5, 1]) == [2, 2, 2, 2, 2, 1, 7]
