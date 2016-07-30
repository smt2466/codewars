# pylint: disable=missing-docstring

"""Equal Sides Of An Array"""

import pytest

from python2.kyu_6.equal_sides_of_an_array import find_even_index

EXAMPLES = (
    ('array', 'expected'),
    [
        ([1, 2, 3, 4, 3, 2, 1], 3),
        ([1, 100, 50, -51, 1, 1], 1),
        ([1, 2, 3, 4, 5, 6], -1),
        ([20, 10, 30, 10, 10, 15, 35], 3),
        ([20, 10, -80, 10, 10, 15, 35], 0),
        ([10, -80, 10, 10, 15, 35, 20], 6),
        (range(1, 100), -1),
        ([0, 0, 0, 0, 0], 0),
        ([-1, -2, -3, -4, -3, -2, -1], 3),
        (range(-100, -1), -1)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(array, expected):
    assert find_even_index(array) == expected
