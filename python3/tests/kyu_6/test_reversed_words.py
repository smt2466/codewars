# pylint: disable=missing-docstring

"""Reversed Words"""

import pytest

from python3.src.kyu_6.reversed_words import reverseWords

EXAMPLES = (
    ('line', 'expected'),
    [
        ('hello world!', 'world! hello'),
        ('The greatest victory is that which requires no battle',
         'battle no requires which that is victory greatest The')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(line, expected):
    assert reverseWords(line) == expected
