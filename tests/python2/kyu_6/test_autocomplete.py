# pylint: disable=missing-docstring

"""Autocomplete! Yay!"""

import pytest

from python2.kyu_6.autocomplete import autocomplete

DICTIONARY = [
    'abnormal',
    'arm-wrestling',
    'absolute',
    'airplane',
    'airport',
    'amazing',
    'apple',
    'ball'
]

EXAMPLES = (
    ('start', 'suggestions'),
    [
        ('ai', ['airplane', 'airport']),
        ('a', ['abnormal', 'arm-wrestling', 'absolute', 'airplane', 'airport'])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(start, suggestions):
    assert autocomplete(start, DICTIONARY) == suggestions


def test_not_a_letter_input():
    assert autocomplete('&a', ['abc', 'def', 'agh']) == ['abc', 'agh']


def test_ignore_letter_case():
    assert autocomplete('a', ['Ab', 'ac', 'ba']) == ['Ab', 'ac']
