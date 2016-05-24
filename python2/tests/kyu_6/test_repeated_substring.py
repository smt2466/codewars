# coding=utf-8
# pylint: disable=missing-docstring, invalid-name

"""
Repeated Substring
"""

from python2.src.kyu_6.repeated_substring import f


def test_simple_multiple_occurrence():
    assert f('ababab') == ('ab', 3)


def test_no_substring():
    assert f('abcde') == ('abcde', 1)


def test_no_substring_but_duplicates():
    assert f('ababc') == ('ababc', 1)
