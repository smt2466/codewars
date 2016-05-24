# pylint: disable=missing-docstring

"""Multiplication Tables"""

import pytest

from python2.src.kyu_6.multiplication_table import multiplication_table

EXAMPLES = (
    ('rows', 'cols', 'table'),
    [
        (2, 2, [[1, 2], [2, 4]]),
        (3, 3, [[1, 2, 3], [2, 4, 6], [3, 6, 9]]),
        (3, 4, [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]])  # Not squared
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(rows, cols, table):
    assert multiplication_table(rows, cols) == table
