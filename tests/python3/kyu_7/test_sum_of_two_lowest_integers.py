# pylint: disable=missing-docstring

"""Sum of two lowest integers"""

import pytest

from python3.kyu_7.sum_of_two_lowest_integers import sum_two_smallest_numbers

EXAMPLES = (
    ('numbers', 'expected'),
    [
        ([5, 8, 12, 18, 22], 13),
        ([7, 15, 12, 18, 22], 19),
        ([25, 42, 12, 18, 22], 30),
        ([1, 8, 12, 18, -1], 0),
        ([-1, -1], -2),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(numbers, expected):
    assert sum_two_smallest_numbers(numbers) == expected
