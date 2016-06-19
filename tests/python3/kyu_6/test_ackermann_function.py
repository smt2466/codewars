# pylint: disable=missing-docstring, invalid-name

"""Ackermann Function"""

import pytest

from python3.kyu_6.ackermann_function import Ackermann

EXAMPLES = (
    ('m', 'n', 'expected'),
    [
        (1, 1, 3),
        (4, 0, 13),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(m, n, expected):
    assert Ackermann(m, n) == expected
