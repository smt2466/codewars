# pylint: disable=missing-docstring

"""Ninja vs Samurai: Attack + Block"""

import pytest

from python3.kyu_5.ninja_vs_samurai_attack_plus_block import Warrior


@pytest.fixture
def ninja():
    return Warrior('Hanzo Hattori')


@pytest.fixture
def samurai():
    return Warrior('Ryōma Sakamoto')


def test_basic_attack(ninja, samurai):
    samurai.block = 'l'
    ninja.attack(samurai, 'h')
    assert samurai.health == 90
