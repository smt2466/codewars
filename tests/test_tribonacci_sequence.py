# pylint: disable=missing-docstring

"""Tribonacci Sequence"""

import pytest

from src.tribonacci_sequence import tribonacci

EXAMPLES = (
    ('expected', 'args', 'num', 'comment'),
    [
        ([1, 1, 1, 3, 5, 9, 17, 31, 57, 105], [1, 1, 1], 10, 'all ones'),
        ([0, 0, 1, 1, 2, 4, 7, 13, 24, 44], [0, 0, 1], 10, 'zero zero one'),
        ([0, 1, 1, 2, 4, 7, 13, 24, 44, 81], [0, 1, 1], 10, 'zero one one'),
        ([], [1, 1, 1], 0, 'empty array'),
        ([1, 2], [1, 2, 3], 2, 'n is less than 3'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_starts_with_all_ones(expected, args, num, comment):
    assert expected == tribonacci(args, num), comment
