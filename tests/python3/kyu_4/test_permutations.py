# pylint: disable=missing-docstring

"""Permutations"""

import pytest

from python3.kyu_4.permutations import permutations


EXAMPLES = (
    ('string', 'expected'),
    [
        ('a', ('a',)),
        ('ab', ('ab', 'ba')),
        ('aabb', ('aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa')),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(string, expected):
    assert permutations(string) == expected
