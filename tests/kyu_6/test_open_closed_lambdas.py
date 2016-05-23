# pylint: disable=missing-docstring

""""Lambdas as a mechanism for Open/Closed"""

from src.kyu_6.open_closed_lambdas import spoken, shouted, whispered, greet


def test_spoken():
    assert spoken('hellO') == 'Hello.'


def test_shouted():
    assert shouted('hellO') == 'HELLO!'


def test_whispered():
    assert whispered('hellO') == 'hello.'


def test_greet_and_spoken():
    assert greet(spoken, 'Hello') == 'Hello.'


def test_greet_and_shouted():
    assert greet(shouted, 'Hello') == 'HELLO!'


def test_greet_and_whispered():
    assert greet(whispered, 'Hello') == 'hello.'
