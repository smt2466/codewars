# pylint: disable=missing-docstring

"""Holiday VIII - Duty Free."""

import pytest

from python3.kyu_8.holiday_viii_duty_free import duty_free

EXAMPLES = (
    ('args', 'expected'),
    [
        ((12, 50, 1000), 166),
        ((17, 10, 500), 294),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert duty_free(*args) == expected
