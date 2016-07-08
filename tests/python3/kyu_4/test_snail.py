# pylint: disable=missing-docstring

"""Snail"""

import pytest

from python3.kyu_4.snail import snail


EXAMPLES = (
    ('array', 'expected'),
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3], [8, 9, 4], [7, 6, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[1, 2], [4, 3]], [1, 2, 3, 4]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(array, expected):
    assert snail(array) == expected
