# pylint: disable=missing-docstring

"""The Shell Game"""

import pytest

from python3.kyu_6.the_shell_game import find_the_ball

EXAMPLES = (
    ('pos', 'swaps', 'expected'),
    [
        (5, [], 5),
        (0, [(0, 1), (2, 1), (0, 1)], 2),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(pos, swaps, expected):
    assert find_the_ball(pos, swaps) == expected
