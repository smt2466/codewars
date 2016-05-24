# pylint: disable=missing-docstring

"""Triangle Number Check"""

import pytest

from python2.src.kyu_6.triangle_number_check import is_triangle_number

EXAMPLES = (
    ('number', 'expected'),
    [
        (3, True),
        (5, False),
        ('hello', False),
        (6.15, False),
        (1, 1)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, expected):
    assert is_triangle_number(number) == expected
