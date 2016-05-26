# pylint: disable=missing-docstring

"""Cycle Detection: greedy algorithm"""

from python2.kyu_6.cycle_detection import cycle


def test_finds_cycle():
    assert cycle([1, 2, 3, 4, 2, 3, 4]) == [1, 3]


def test_no_previous_chars():
    assert cycle([2, 3, 4, 2, 3, 4]) == [0, 3]


def test_no_cycle():
    assert cycle([1, 2, 3, 4]) == []


def test_duplication():
    assert cycle([1, 1, 1, 1, 1, 1, 1, 1]) == [0, 1]
