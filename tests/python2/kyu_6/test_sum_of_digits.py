# pylint: disable=missing-docstring

"""Sum of Digits / Digital Root"""

import pytest

from src.python2.kyu_6.sum_of_digits import digital_root

EXAMPLES = (
    ('number', 'expected'),
    [
        (16, 7),
        (942, 6),
        (132189, 6),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, expected):
    assert digital_root(number) == expected
