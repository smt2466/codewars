# pylint: disable=missing-docstring

"""Calculator"""

import pytest

from python2.kyu_3.calculator import Calculator


EXAMPLES = (
    ('code', 'expected'),
    [
        ('2 / 2 + 3 * 4 - 6', 7),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(code, expected):
    assert Calculator().evaluate(code) == expected
