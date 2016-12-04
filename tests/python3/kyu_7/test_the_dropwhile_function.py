# pylint: disable=missing-docstring

"""The dropWhile Function"""

import pytest

from python3.kyu_7.the_dropwhile_function import drop_while


def is_even(num):
    return not num % 2


def is_odd(num):
    return num % 2


EXAMPLES = (
    ('arr', 'pred', 'expected'),
    [
        ([2, 6, 4, 10, 1, 5, 4, 3], is_even, [1, 5, 4, 3]),
        ([2, 100, 1000, 10000, 10000, 5, 3, 4, 6], is_even, [5, 3, 4, 6]),
        ([998, 996, 12, -1000, 200, 0, 1, 1, 1], is_even, [1, 1, 1]),
        ([1, 4, 2, 3, 5, 4, 5, 6, 7], is_even, [1, 4, 2, 3, 5, 4, 5, 6, 7]),
        ([2, 4, 10, 100, 64, 78, 92], is_even, []),
        ([1, 2, 3, 4, 5], is_odd, [2, 3, 4, 5]),
        ([1, 5, 111, 1111, 1111, 2, 4, 6, 4, 5], is_odd, [2, 4, 6, 4, 5]),
        ([-1, -5, 127, 86, 902, 2, 1], is_odd, [86, 902, 2, 1]),
        ([2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0], is_odd,
         [2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0]),
        ([1, 3, 5, 7, 9, 111], is_odd, [])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arr, pred, expected):
    assert drop_while(arr, pred) == expected
