# pylint: disable=missing-docstring

"""Counting Duplicates"""

import pytest

from python2.kyu_6.counting_duplicates import duplicate_count

EXAMPLES = (
    ('text', 'expected'),
    [
        ('abcde', 0),
        ('abcdea', 1),
        ('indivisibility', 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert duplicate_count(text) == expected
