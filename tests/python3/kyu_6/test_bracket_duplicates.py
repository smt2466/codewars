# pylint: disable=missing-docstring

"""Bracket Duplicates"""

import pytest

from python3.kyu_6.bracket_duplicates import string_parse

EXAMPLES = (
    ('string', 'expected'),
    [
        ('a', 'a'),
        ('aa', 'aa'),
        ('aaa', 'aa[a]'),
        ('aaaabbcdefffffffg', 'aa[aa]bbcdeff[fffff]g')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(string, expected):
    assert string_parse(string) == expected
