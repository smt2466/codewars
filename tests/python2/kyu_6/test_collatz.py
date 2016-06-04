# pylint: disable=missing-docstring

"""Collatz"""

import pytest

from python2.kyu_6.collatz import collatz

EXAMPLES = (
    ('num', 'expected'),
    [
        (1, '1'),
        (3, '3->10->5->16->8->4->2->1'),
        (4, '4->2->1'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, expected):
    assert collatz(num) == expected
