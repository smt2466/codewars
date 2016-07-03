# pylint: disable=missing-docstring, invalid-name

"""Roman Numerals Helper"""

import pytest

from python2.kyu_4.roman_numerals_helper import RomanNumerals


TO_ROMAN = (
    ('number', 'expected'),
    [
        (1, 'I'),
        (2, 'II'),
        (4, 'IV'),
        (5, 'V'),
        (9, 'IX'),
    ]
)


FROM_ROMAN = (
    ('number', 'expected'),
    [
        ('I', 1),
        ('II', 2),
        ('IV', 4),
        ('V', 5),
        ('IX', 9),
    ]
)


@pytest.mark.parametrize(*TO_ROMAN)
def test_to_roman_returns_correct_result(number, expected):
    assert RomanNumerals.to_roman(number) == expected


@pytest.mark.parametrize(*FROM_ROMAN)
def test_from_roman_returns_correct_result(number, expected):
    assert RomanNumerals.from_roman(number) == expected
