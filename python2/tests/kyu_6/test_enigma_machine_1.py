# pylint: disable=missing-docstring, redefined-outer-name, invalid-name

"""The Enigma Machine - Part 1: The Plugboard"""

import pytest

from python2.src.kyu_6.enigma_machine_1 import Plugboard


@pytest.fixture()
def plugboard():
    return Plugboard('AB')


def test_pair_is_wired(plugboard):
    assert plugboard.process('A') == 'B'
    assert plugboard.process('B') == 'A'


def test_unpaired_char(plugboard):
    assert plugboard.process('C') == 'C'


def test_too_many_wires():
    with pytest.raises(ValueError):
        Plugboard('ABCDEFGHIJKLMNOPQRSTUV')


def test_empty_construction():
    assert Plugboard().process('A') == 'A'


def test_char_can_be_wired_only_once():
    with pytest.raises(ValueError):
        Plugboard('ABAB')
