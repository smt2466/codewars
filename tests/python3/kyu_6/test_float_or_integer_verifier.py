# pylint: disable=missing-docstring

"""Float or Integer verifier"""

import pytest

from python3.kyu_6.float_or_integer_verifier import i_or_f

EXAMPLES = (
    ('number', 'expected'),
    [
        ('1', True),
        ('1.0', True),
        ('1e1', True),
        ('1E-1', True),
        ('1e+1', True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, expected):
    assert i_or_f(number) == expected
