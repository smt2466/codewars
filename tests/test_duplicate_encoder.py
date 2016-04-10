# pylint: disable=missing-docstring

""""Duplicate Encoder"""

import pytest

from src.duplicate_encoder import duplicate_encode

EXAMPLES = (
    ('text', 'expected'),
    [
        ('din', '((('),
        ('recede', '()()()'),
        ('Success', ')())())'),  # Ignoring case
        ('(( @', '))((')         # Special characters
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert duplicate_encode(text) == expected
