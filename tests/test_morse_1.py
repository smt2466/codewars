# pylint: disable=missing-docstring

"""Decode the Morse code"""

import pytest

from src.morse_1 import decodeMorse

EXAMPLES = (
    ('code', 'expected'),
    [
        ('.... . -.--   .--- ..- -.. .', 'HEY JUDE'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(code, expected):
    assert decodeMorse(code) == expected
