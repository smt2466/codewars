# pylint: disable=missing-docstring

"""Take a Number And Sum Its Digits Raised To The Consecutive Powers"""

import pytest

from python2.kyu_6.consecutive_powers import check_powers, sum_dig_pow

NUMBERS = (
    ('number', 'expected'),
    [
        (5, True),
        (89, True),
        (135, True),
        (11, False),
    ]
)

RANGES = (
    ('start', 'stop', 'expected'),
    [
        (1, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (1, 100, [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]),
        (10, 89, [89]),
        (10, 100, [89]),
        (90, 100, []),
        (89, 135, [89, 135]),
    ]
)


@pytest.mark.parametrize(*NUMBERS)
def test_check_powers(number, expected):
    assert check_powers(number) == expected


@pytest.mark.parametrize(*RANGES)
def test_returns_correct_list(start, stop, expected):
    assert sum_dig_pow(start, stop) == expected
