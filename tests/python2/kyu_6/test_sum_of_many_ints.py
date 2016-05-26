# pylint: disable=missing-docstring

"""Sum of many ints"""

import pytest

from python2.kyu_6.sum_of_many_ints import f

EXAMPLES = (
    ('limit', 'divisor', 'expected'),
    [
        (10, 5, 20),
        (20, 20, 190),
        (15, 10, 60),
        (59883586.0, 46240761.0, 1162167309620905)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(limit, divisor, expected):
    assert f(limit, divisor) == expected
