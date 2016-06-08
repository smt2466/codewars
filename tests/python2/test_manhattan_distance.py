# pylint: disable=missing-docstring

"""Manhattan Distance"""

import pytest

from python2.kyu_6.manhattan_distance import manhattan_distance

EXAMPLES = (
    ('point1', 'point2', 'expected'),
    [
        ([1, 1], [1, 1], 0),
        ([5, 4], [3, 2], 4),
        ([1, 1], [0, 3], 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(point1, point2, expected):
    assert manhattan_distance(point1, point2) == expected
