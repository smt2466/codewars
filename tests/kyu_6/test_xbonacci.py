# pylint: disable=missing-docstring

"""Fibonacci, Tribonacci and friends"""

import pytest

from src.kyu_6.xbonacci import Xbonacci

EXAMPLES = (
    ('signature', 'number', 'expected'),
    [
        ([0, 1], 10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
        ([1, 1], 10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
        ([0, 0, 0, 0, 1], 10, [0, 0, 0, 0, 1, 1, 2, 4, 8, 16]),
        ([1, 0, 0, 0, 0, 0, 1], 10, [1, 0, 0, 0, 0, 0, 1, 2, 3, 6]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(signature, number, expected):
    assert Xbonacci(signature, number) == expected
