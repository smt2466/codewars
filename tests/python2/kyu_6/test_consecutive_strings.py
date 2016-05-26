# pylint: disable=missing-docstring

"""Consecutive strings"""

from python2.kyu_6.consecutive_strings import longest_consec


def test_returns_correct_result():
    strarr = ['zone', 'abigail', 'theta', 'form', 'libe', 'zas']
    expected = 'abigailtheta'
    assert longest_consec(strarr, 2) == expected


def test_one_item():
    strarr = ['ejjjjmmtthh', 'zxxuueeg', 'aanlljrrrxx', 'dqqqaaabbb',
              'oocccffuucccjjjkkkjyyyeehh']
    expected = 'oocccffuucccjjjkkkjyyyeehh'
    assert longest_consec(strarr, 1) == expected


def test_empty_strarr():
    assert longest_consec([], 3) == ''


def test_long_strings():
    strarr = ['itvayloxrp', 'wkppqsztdkmvcuwvereiupccauycnjutlv',
              'vweqilsfytihvrzlaodfixoyxvyuyvgpck']
    expected = 'wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfix' \
               'oyxvyuyvgpck'
    assert longest_consec(strarr, 2) == expected


def test_first_two_are_longest():
    strarr = ['wlwsasphmxx', 'owiaxujylentrklctozmymu', 'wpgozvxxiu']
    expected = 'wlwsasphmxxowiaxujylentrklctozmymu'
    assert longest_consec(strarr, 2) == expected


def test_negative_consecutive_num():
    strarr = ['zone', 'abigail', 'theta', 'form', 'libe', 'zas']
    assert longest_consec(strarr, -2) == ''


def test_three_consecutive():
    strarr = ['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz']
    expected = 'ixoyx3452zzzzzzzzzzzz'
    assert longest_consec(strarr, 3) == expected


def test_big_consecutive_num():
    strarr = ['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz']
    assert longest_consec(strarr, 15) == ''


def test_consecutive_num_is_zero():
    strarr = ['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz']
    assert longest_consec(strarr, 0) == ''
