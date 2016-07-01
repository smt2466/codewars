# pylint: disable=missing-docstring

"""Roman Numerals Encoder"""

import pytest

from python2.kyu_4.roman_numerals_encoder import solution


EXAMPLES = (
    ('number', 'expected'),
    [
        (1000, 'M'),
        (1, 'I'),
        (4, 'IV'),
        (6, 'VI'),
        (89, 'LXXXIX'),
        (9, 'IX'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, expected):
    assert solution(number) == expected
