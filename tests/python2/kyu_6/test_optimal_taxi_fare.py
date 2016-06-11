# pylint: disable=missing-docstring

"""Optimal Taxi Fare"""

import pytest

from python2.kyu_6.optimal_taxi_fare import calculate_optimal_fare

EXAMPLES = (
    ('args', 'expected'),
    [
        ((8, 10, 90, 2, 6), '15.00'),
        ((100, 10, 500, 5, 25), 'Won\'t make it!'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert calculate_optimal_fare(*args) == expected
