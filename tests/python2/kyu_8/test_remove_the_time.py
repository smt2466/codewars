# coding=utf-8
# pylint: disable=missing-docstring

"""
Remove the Time Kata tests
"""

from src.python2.kyu_8.remove_the_time import shorten_to_date


def test_one_digit_day_number():
    assert shorten_to_date('Monday February 2, 8pm') == 'Monday February 2'


def test_two_digit_day_number():
    assert shorten_to_date('Tuesday May 29, 8pm') == 'Tuesday May 29'


def test_two_digit_hour():
    assert shorten_to_date('Tuesday January 29, 10pm') == 'Tuesday January 29'


def test_am_time():
    assert shorten_to_date('Friday May 2, 9am') == 'Friday May 2'


def test_short_week_day():
    assert shorten_to_date('Wed September 1, 3am') == 'Wed September 1'
