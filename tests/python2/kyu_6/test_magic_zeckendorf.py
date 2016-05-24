# pylint: disable=missing-docstring

"""Magic Zeckendorf"""

from src.python2.kyu_6.magic_zeckendorf import magicZ

ZZ = magicZ()


def test_guesses_correct_number():
    assert ZZ.gueZZ([1, 5, 8]) == 70


def test_returns_correct_cards():
    assert sorted(ZZ.get_magicZ_index(70)) == [1, 5, 8]


def test_ignore_duplicate_cards():
    assert ZZ.gueZZ([1, 1, 5, 5, 8, 8, 8]) == 70


def test_fewer_cards_than_expected():
    assert ZZ.gueZZ() == 0
