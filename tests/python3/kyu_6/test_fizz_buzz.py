# pylint: disable=missing-docstring

"""Fizz / Buzz"""

import pytest

from python3.kyu_6.fizz_buzz import solution

EXAMPLES = (
    ('number', 'expected'),
    [
        (20, [5, 2, 1]),
        (2, [0, 0, 0]),
        (30, [8, 4, 1]),
        (300, [80, 40, 19]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, expected):
    assert solution(number) == expected
