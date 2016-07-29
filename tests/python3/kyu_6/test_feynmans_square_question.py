# pylint: disable=missing-docstring

"""Feynman's square question"""

import pytest

from python3.kyu_6.feynmans_square_question import count_squares

EXAMPLES = (
    ('num', 'expected'),
    [
        (1, 1),
        (2, 5),
        (3, 14),
        (5, 55),
        (8, 204),
        (15, 1240),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, expected):
    assert count_squares(num) == expected
