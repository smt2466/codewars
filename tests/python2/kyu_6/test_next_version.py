# coding=utf-8
# pylint: disable=missing-docstring

"""
Next version
"""

from src.python2.kyu_6.next_version import next_version


def test_simple_incrementing():
    assert next_version('1.2.3') == '1.2.4'


def test_increment_multiple():
    assert next_version('0.9.9') == '1.0.0'


def test_one_digit_version():
    assert next_version('1') == '2'


def test_long_version():
    assert next_version('1.2.3.4.5.6.7.8') == '1.2.3.4.5.6.7.9'


def test_next_version():
    assert next_version('9.9') == '10.0'


def test_version_with_last_9():
    assert next_version('9.9.9.9.9.9.9.8') == '9.9.9.9.9.9.9.9'


def test_one_multi_digit_number():
    assert next_version('10') == '11'


def test_long_multi_digit_number():
    assert next_version('302025720259') == '302025720260'


def test_last_multi_digit_number():
    assert next_version('10.9.9.9.9.9') == '11.0.0.0.0.0'
