# pylint: disable=missing-docstring

"""Duck Duck Goose"""

import pytest

from python3.kyu_8.duck_duck_goose import duck_duck_goose, Player

PLAYERS = [Player('a'), Player('b'), Player('c')]

EXAMPLES = (
    ('players', 'goose', 'expected'),
    [
        (PLAYERS, 1, 'a'),
        (PLAYERS, 2, 'b'),
        (PLAYERS, 3, 'c'),
        (PLAYERS, 4, 'a'),
        (PLAYERS, 8, 'b'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(players, goose, expected):
    assert duck_duck_goose(players, goose) == expected
