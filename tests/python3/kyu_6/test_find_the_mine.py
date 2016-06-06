# pylint: disable=missing-docstring

"""Find the Mine!"""

import pytest

from python3.kyu_6.find_the_mine import mineLocation

EXAMPLES = (
    ('field', 'expected'),
    [
        ([[1, 0], [0, 0]], [0, 0]),
        ([[1, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0]),
        ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]], [2, 2]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(field, expected):
    assert mineLocation(field) == expected
