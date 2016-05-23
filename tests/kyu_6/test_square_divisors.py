# pylint: disable=missing-docstring

"""Integers: Recreation One"""

import pytest

from src.kyu_6.square_divisors import list_squared

EXAMPLES = (
    ('start', 'stop', 'expected'),
    [
        (1, 250, [[1, 1], [42, 2500], [246, 84100]]),
        (42, 250, [[42, 2500], [246, 84100]]),
        (250, 500, [[287, 84100]]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(start, stop, expected):
    assert list_squared(start, stop) == expected
