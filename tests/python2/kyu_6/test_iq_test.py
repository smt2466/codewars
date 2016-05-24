# pylint: disable=missing-docstring

""""IQ Test"""

import pytest

from src.python2.kyu_6.iq_test import iq_test

EXAMPLES = (
    ('numbers', 'expected'),
    [
        ('2 4 7 8 10', 3),
        ('1 2 2', 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(numbers, expected):
    assert iq_test(numbers) == expected
