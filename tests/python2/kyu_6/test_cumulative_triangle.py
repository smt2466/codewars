# pylint: disable=missing-docstring

"""Cumulative Triangle"""

import pytest

from python2.kyu_6.cumulative_triangle import cumulative_triangle

EXAMPLES = (
    ('row', 'expected'),
    [
        (1, 1),
        (3, 15),
        (4, 34),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(row, expected):
    assert cumulative_triangle(row) == expected
