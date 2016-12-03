# pylint: disable=missing-docstring

"""BASIC: Making Six Toast."""

import pytest

from python3.kyu_8.basic_making_six_toast import six_toasts

EXAMPLES = (
    ('num', 'expected'),
    [
        (15, 9),
        (6, 0),
        (3, 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, expected):
    assert six_toasts(num) == expected
