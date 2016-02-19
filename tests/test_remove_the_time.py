# coding=utf-8

"""
Remove the Time Kata tests
"""

from src.remove_the_time import shorten_to_date


def test_one_digit_day_number():
    assert 'Monday February 2' == shorten_to_date('Monday February 2, 8pm')


def test_two_digit_day_number():
    assert 'Tuesday May 29' == shorten_to_date('Tuesday May 29, 8pm')


def test_two_digit_hour():
    assert 'Tuesday January 29' == shorten_to_date('Tuesday January 29, 10pm')


def test_am_time():
    assert 'Friday May 2' == shorten_to_date('Friday May 2, 9am')

def test_short_week_day():
    assert 'Wed September 1' == shorten_to_date('Wed September 1, 3am')
