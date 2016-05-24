# pylint: disable=missing-docstring

"""Multi-tap Keypad Text Entry on an Old Mobile Phone"""

import pytest

from python2.src.kyu_6.multi_tap import presses

EXAMPLES = (
    ('message', 'taps'),
    [
        ('LOL', 9),
        ('HOW R U', 13),
        ('WHERE DO U WANT 2 MEET L8R', 47)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(message, taps):
    assert presses(message) == taps
