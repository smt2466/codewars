# pylint: disable=missing-docstring

"""Palindrome chain length"""

import pytest

from python3.kyu_5.palindrome_chain_length import (
    palindrome,
    palindrome_chain_length
)

EXAMPLES = (
    ('number', 'expected'),
    [
        (87, 4),
    ]
)

PALINDROMES = (
    ('number', 'expected'),
    [
        (5, True),
        (44, True),
        (171, True),
        (4884, True),
        (43, False),
        (194, False),
        (4773, False),
    ]
)


@pytest.mark.parametrize(*PALINDROMES)
def test_palindrome_returns_correct_result(number, expected):
    assert palindrome(number) == expected


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, expected):
    assert palindrome_chain_length(number) == expected
