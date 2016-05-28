# pylint: disable=missing-docstring

"""Round by 0.5 steps"""

import pytest

from python2.kyu_6.round_by_point_5 import solution

EXAMPLES = (
    ('num', 'expected'),
    [
        (4.2, 4),
        (4.25, 4.5),
        (4.4, 4.5),
        (4.6, 4.5),
        (4.75, 5),
        (4.8, 5),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, expected):
    assert solution(num) == expected
