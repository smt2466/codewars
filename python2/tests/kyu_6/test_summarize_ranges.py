# pylint: disable=missing-docstring

""""Summarize ranges"""

from python2.src.kyu_6.summarize_ranges import summary_ranges


def test_empty_array():
    assert summary_ranges([]) == []


def test_all_items_equal():
    assert summary_ranges([1, 1, 1, 1]) == ['1']


def test_one_range():
    assert summary_ranges([1, 2, 3, 4]) == ['1->4']


def test_one_big_range():
    assert summary_ranges([0, 1, 2, 3, 4, 5, 6, 7]) == ['0->7']


def test_multiple_ranges():
    assert summary_ranges([0, 1, 2, 5, 6, 9]) == ['0->2', '5->6', '9']


def test_negative_numbers():
    task = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 12]
    answer = ['-2', '0->7', '9->10', '12']
    assert summary_ranges(task) == answer
