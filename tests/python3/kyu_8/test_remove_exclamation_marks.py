# pylint: disable=missing-docstring

"""Remove exclamation marks"""

import pytest

from python3.kyu_8.remove_exclamation_marks import remove_exclamation_marks

EXAMPLES = (
    ('strng', 'expected'),
    [
        ('Hello World!', 'Hello World'),
        ('Hello World!!!', 'Hello World'),
        ('Hi! Hello!', 'Hi Hello'),
        ("", ""),
        ('Oh, no!!!', 'Oh, no'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(strng, expected):
    assert remove_exclamation_marks(strng) == expected
