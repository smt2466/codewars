# pylint: disable=missing-docstring

"""Decode the Morse code"""

import pytest

from python2.src.kyu_6.morse_1 import decodeMorse

EXAMPLES = (
    ('code', 'expected'),
    [
        ('.... . -.--   .--- ..- -.. .', 'HEY JUDE'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(code, expected):
    assert decodeMorse(code) == expected
