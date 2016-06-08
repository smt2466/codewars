# pylint: disable=missing-docstring

import pytest

from python3.kyu_6.nth_fibonacci import nth_fib

EXAMPLES = (
    ('num', 'expected'),
    [
        (1, 0),
        (2, 1),
        (4, 2),
        (8, 13),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, expected):
    assert nth_fib(num) == expected
