# pylint: disable=missing-docstring

"""WeIrD StRiNg CaSe"""

from src.kyu_6.weird_string_case import to_weird_case


def test_word_starts_with_upper():
    assert to_weird_case('This') == 'ThIs'


def test_word_starts_with_lower():
    assert to_weird_case('is') == 'Is'


def test_multiple_words():
    assert to_weird_case('This is a test') == 'ThIs Is A TeSt'
