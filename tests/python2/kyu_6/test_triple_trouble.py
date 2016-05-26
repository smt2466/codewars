# pylint: disable=missing-docstring

"""Triple trouble"""

import pytest

from python2.kyu_6.triple_trouble import triple_double

EXAMPLES = (
    ('num1', 'num2', 'expected'),
    [
        (451999277, 41177722899, 1),
        (1222345, 12345, 0),
        (12345, 12345, 0),
        (666789, 12345667, 1),
        (10560002, 100, 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num1, num2, expected):
    assert triple_double(num1, num2) == expected
