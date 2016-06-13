# pylint: disable=missing-docstring

"""Simple card game"""

import pytest

from python2.kyu_6.simple_card_game import winner

EXAMPLES = (
    ('deck_steve', 'deck_josh', 'expected'),
    [
        (['A', '7', '8'], ['K', '5', '9'], 'Steve wins 2 to 1'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(deck_steve, deck_josh, expected):
    assert winner(deck_steve, deck_josh) == expected
