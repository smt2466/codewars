# pylint: disable=missing-docstring

"""Hamming Distance"""

import pytest

from python3.kyu_6.hamming_distance import hamming

EXAMPLES = (
    ('text1', 'text2', 'expected'),
    [
        ('I like turtles', 'I like turkeys', 3),
        ('Hello World', 'Hello World', 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text1, text2, expected):
    assert hamming(text1, text2) == expected
