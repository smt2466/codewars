# pylint: disable=missing-docstring

"""Detect Pangram"""

import pytest

from python3.kyu_6.detect_pangram import is_pangram

EXAMPLES = (
    ('text', 'expected'),
    [
        ('The quick, brown fox jumps over the lazy dog!', True),
        ('Hello world', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert is_pangram(text) == expected
