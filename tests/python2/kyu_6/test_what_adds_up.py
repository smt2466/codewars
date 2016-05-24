# coding=utf-8
# pylint: disable=invalid-name, missing-docstring

""""
What adds up
"""

from src.python2.kyu_6.what_adds_up import addsup


def compare_arrays(a1, a2):
    if len(a1) != len(a2) or sorted(a1) != sorted(a2):
        return False
    else:
        return True


def test_returns_correct_result():
    task = [[1, 2, 5], [3, 1], [5, 4, 6]]
    answer = [[1, 3, 4], [2, 3, 5], [5, 1, 6]]
    assert compare_arrays(addsup(*task), answer) is True
