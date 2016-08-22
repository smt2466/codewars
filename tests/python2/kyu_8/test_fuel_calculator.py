# pylint: disable=missing-docstring

"""Fuel Calculator """

import pytest

from python2.kyu_8.fuel_calculator import fuelPrice

EXAMPLES = (
    ('litres', 'price', 'expected'),
    [
        (10, 21.5, 212.50),
        (40, 10, 390.00),
        (15, 5.83, 83.70),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(litres, price, expected):
    assert fuelPrice(litres, price) == expected
