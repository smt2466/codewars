# pylint: disable=missing-docstring

"""Tortoise racing"""

import pytest

from python3.kyu_6.tortoise_racing import race

EXAMPLES = (
    ('speed1', 'speed2', 'lead', 'expected'),
    [
        (720, 850, 70, [0, 32, 18]),
        (80, 91, 37, [3, 21, 49]),
        (80, 100, 40, [2, 0, 0]),
        (820, 81, 550, None)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(speed1, speed2, lead, expected):
    assert race(speed1, speed2, lead) == expected
