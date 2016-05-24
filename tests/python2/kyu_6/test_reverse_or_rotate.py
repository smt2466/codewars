# pylint: disable=missing-docstring

"""Reverse or rotate?"""

import pytest

from src.python2.kyu_6.reverse_or_rotate import revrot

EXAMPLES = (
    ('string', 'size', 'expected'),
    [
        ('1234', 0, ''),
        ('', 0, ''),
        ('1234', 5, ''),
        ('733049910872815764', 5, '330479108928157'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(string, size, expected):
    assert revrot(string, size) == expected
