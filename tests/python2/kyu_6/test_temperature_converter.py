# coding=utf-8
# pylint: disable=missing-docstring

"""
Temperature converter
"""

from src.python2.kyu_6.temperature_converter import convert_temp


def test_celsius_fahrenheit():
    assert convert_temp(100, "C", "F") == 212


def test_delisle_kelvin():
    assert convert_temp(-30, "De", "K") == 393


def test_reaumur_celsius():
    assert convert_temp(40, "Re", "C") == 50


def test_delisle_fahrenheit():
    assert convert_temp(60, "De", "F") == 140


def test_kelvin_newton():
    assert convert_temp(373.15, "K", "N") == 33


def test_kelvin_kelvin():
    assert convert_temp(373.15, "K", "N") == 33
