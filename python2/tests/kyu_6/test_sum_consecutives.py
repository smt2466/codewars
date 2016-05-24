# pylint: disable=missing-docstring

"""Sum consecutives"""

import pytest

from python2.src.kyu_6.sum_consecutives import sum_consecutives

EXAMPLES = (
    ('sequence', 'expected'),
    [
        ([1, 4, 4, 4, 0, 4, 3, 3, 1], [1, 12, 0, 4, 6, 1]),
        ([1, 1, 7, 7, 3], [2, 14, 3]),
        ([-5, -5, 7, 7, 12, 0], [-10, 14, 12, 0]),
        ([3, 3, 3, 3, 1], [12, 1])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(sequence, expected):
    assert sum_consecutives(sequence) == expected
