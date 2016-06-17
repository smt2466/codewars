# pylint: disable=missing-docstring

"""Frog jumping"""

import pytest

from python2.kyu_6.frog_jumping import solution

EXAMPLES = (
    ('array', 'expected'),
    [
        ([1, 2, 2, -1], 4),
        ([1, 2, 1, 5], 3),
        ([1, -1], -1),
        ([-1, 1], 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(array, expected):
    assert solution(array) == expected
