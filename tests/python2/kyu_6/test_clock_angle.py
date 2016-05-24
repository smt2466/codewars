# coding=utf-8
# pylint: disable=missing-docstring, invalid-name

""""
Angle Between Clock Hands
"""

from src.python2.kyu_6.clock_angle import handAngle


def test_midnight():
    assert handAngle(0, 0) == 0


def test_midnight_as_12():
    assert handAngle(12, 0) == 0


def test_six_o_clock():
    assert round(handAngle(6, 0), 11) == 3.14159265359


def test_one_o_clock():
    assert round(handAngle(1, 0), 11) == 0.5235987756


def test_nine_o_clock():
    assert round(handAngle(9, 0), 11) == 1.57079632679


def test_ten_o_clock():
    assert round(handAngle(10, 0), 11) == 1.0471975512


def test_fifteen_minutes_of_midnight():
    assert round(handAngle(0, 15), 11) == 1.4398966329


def test_forty_five_minutes_of_midnight():
    assert round(handAngle(0, 45), 11) == 1.96349540849


def test_thirty_minutes_of_midnight_as_12():
    assert round(handAngle(12, 30), 11) == 2.87979326579


def test_fifteen_minutes_of_seven_o_clock():
    assert round(handAngle(7, 15), 11) == 2.22529479629


def test_five_minutes_of_six_o_clock():
    assert round(handAngle(6, 5), 11) == 2.66162710929
