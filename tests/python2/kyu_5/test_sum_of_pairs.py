# pylint: disable=missing-docstring

"""Sum of Pairs."""

import pytest

from python2.kyu_5.sum_of_pairs import sum_pairs

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1, 4, 8, 7, 3, 15], 8), [1, 7]),
        (([1, -2, 3, 0, -6, 1], -6), [0, -6]),
        (([20, -13, 40], -7), None),
        (([1, 2, 3, 4, 1, 0], 2), [1, 1]),
        (([10, 5, 2, 3, 7, 5], 10), [3, 7]),
        (([4, -2, 3, 3, 4], 8), [4, 4]),
        (([0, 2, 0], 0), [0, 0]),
        (([5, 9, 13, -3], 10), [13, -3]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert sum_pairs(*args) == expected
