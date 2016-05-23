# pylint: disable=missing-docstring

"""Rotate Array (JS)"""

import pytest

from src.kyu_6.rotate_array import rotate

DATA = [1, 2, 3, 4, 5]

POSITIVE = (
    ('shift', 'expected'),
    [
        (1, [5, 1, 2, 3, 4]),
        (2, [4, 5, 1, 2, 3]),
        (3, [3, 4, 5, 1, 2]),
        (4, [2, 3, 4, 5, 1]),
        (5, [1, 2, 3, 4, 5])
    ]
)

NEGATIVE = (
    ('shift', 'expected'),
    [
        (-1, [2, 3, 4, 5, 1]),
        (-2, [3, 4, 5, 1, 2]),
        (-3, [4, 5, 1, 2, 3]),
        (-4, [5, 1, 2, 3, 4]),
        (-5, [1, 2, 3, 4, 5]),
    ]
)

ANY = (
    ('array', 'shift', 'expected'),
    [
        (['a', 'b', 'c'], 1, ['c', 'a', 'b']),
        ([1.0, 2.0, 3.0], 1, [3.0, 1.0, 2.0]),
        ([True, True, False], 1, [False, True, True])
    ]
)

LONG = (
    ('shift', 'expected'),
    [
        (7, [4, 5, 1, 2, 3]),
        (11, [5, 1, 2, 3, 4]),
        (12478, [3, 4, 5, 1, 2]),
    ]
)


@pytest.mark.parametrize(*POSITIVE)
def test_positive_shift(shift, expected):
    assert rotate(DATA, shift) == expected


@pytest.mark.parametrize(*NEGATIVE)
def test_negative_shift(shift, expected):
    assert rotate(DATA, shift) == expected


@pytest.mark.parametrize(*LONG)
def test_big_shift(shift, expected):
    assert rotate(DATA, shift) == expected


@pytest.mark.parametrize(*ANY)
def test_array_contains_anything(array, shift, expected):
    assert rotate(array, shift) == expected


def test_zero_shift():
    assert rotate(DATA, 0) == [1, 2, 3, 4, 5]
