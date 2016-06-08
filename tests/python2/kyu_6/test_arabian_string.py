# pylint: disable=missing-docstring

"""Arabian String"""

import pytest

from python2.kyu_6.arabian_string import camelize

EXAMPLES = (
    ('strng', 'expected'),
    [
        ('java script', 'JavaScript'),
        ('cODE warS', 'CodeWars'),
        ('Rugby:club:2013', 'RugbyClub2013'),
        ('Arabian_string-test', 'ArabianStringTest'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(strng, expected):
    assert camelize(strng) == expected
