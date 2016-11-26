# pylint: disable=missing-docstring

"""Remove First and Last Character"""

import pytest

from python3.kyu_8.remove_first_and_last_character import remove_char

EXAMPLES = (
    ('text', 'expected'),
    [
        ('eloquent', 'loquen'),
        ('country', 'ountr'),
        ('person', 'erso'),
        ('place', 'lac'),
        ('ok', ''),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert remove_char(text) == expected
