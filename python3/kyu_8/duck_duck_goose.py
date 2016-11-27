# pylint: disable=too-few-public-methods

"""Duck Duck Goose
https://www.codewars.com/kata/duck-duck-goose

The objective of "Duck, duck, goose" is to walk in a circle, tapping on each
player's head until one is finally chosen.

Task:

Given an array of Player objects (an array of associative arrays in PHP) and
an index (**1-based**), return the name of the chosen Player.

Example:
    duck_duck_goose([a, b, c, d], 1) should return a.name
    duck_duck_goose([a, b, c, d], 5) should return a.name
    duck_duck_goose([a, b, c, d], 4) should return d.name
"""

from typing import List


class Player:
    """Player representation"""

    def __init__(self, name):
        self.name = name


def duck_duck_goose(players: List[Player], goose: int) -> str:
    """Duck Duck Goose game"""
    return players[(goose - 1) % len(players)].name
