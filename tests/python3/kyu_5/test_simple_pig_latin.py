# pylint: disable=missing-docstring

"""Simple Pig Latin"""

import pytest

from python3.kyu_5.simple_pig_latin import pig_it


EXAMPLES = (
    ('text', 'expected'),
    [
        ('Pig latin is cool', 'igPay atinlay siay oolcay'),
        ('This is my string', 'hisTay siay ymay tringsay'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert pig_it(text) == expected
