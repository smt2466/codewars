# coding=utf-8
# pylint: disable=missing-docstring,invalid-name

""""
80's Kids #1: How Many Licks Does it Take?
"""

from src.kyu_7.kids_80s_1 import total_licks


def test_positive_and_negative_conditions():
    answer = 'It took 260 licks to get to the tootsie roll center of a ' \
             'tootsie pop. The toughest challenge was freezing temps.'
    conditions = {'freezing temps': 10, 'clear skies': -2}
    assert total_licks(conditions) == answer


def test_two_negative_conditions():
    answer = 'It took 245 licks to get to the tootsie roll center of a ' \
             'tootsie pop.'
    conditions = {'happiness': -5, 'clear skies': -2}
    assert total_licks(conditions) == answer


def test_no_conditions():
    answer = 'It took 252 licks to get to the tootsie roll center of a ' \
             'tootsie pop.'
    conditions = {}
    assert total_licks(conditions) == answer


def test_three_positive_conditions():
    answer = 'It took 512 licks to get to the tootsie roll center of a ' \
             'tootsie pop. The toughest challenge was evil wizards.'
    conditions = {'dragons': 100, 'evil wizards': 110, 'trolls': 50}
    assert total_licks(conditions) == answer


def test_one_negative_condition():
    answer = 'It took 2 licks to get to the tootsie roll center of a ' \
             'tootsie pop.'
    conditions = {'white magic': -250}
    assert total_licks(conditions) == answer
