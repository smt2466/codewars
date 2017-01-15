# pylint: disable=missing-docstring

"""Double Cola."""

import pytest

from python3.kyu_5.double_cola import whoIsNext

NAMES = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

EXAMPLES = (
    ('args', 'expected'),
    [
        ((NAMES, 1), 'Sheldon'),
        ((NAMES, 2), 'Leonard'),
        ((NAMES, 3), 'Penny'),
        ((NAMES, 4), 'Rajesh'),
        ((NAMES, 5), 'Howard'),
        ((NAMES, 6), 'Sheldon'),
        ((NAMES, 7), 'Sheldon'),
        ((NAMES, 8), 'Leonard'),
        ((NAMES, 9), 'Leonard'),
        ((NAMES, 10), 'Penny'),
        ((NAMES, 11), 'Penny'),
        ((NAMES, 12), 'Rajesh'),
        ((NAMES, 13), 'Rajesh'),
        ((NAMES, 14), 'Howard'),
        ((NAMES, 15), 'Howard'),
        ((NAMES, 16), 'Sheldon'),
        ((NAMES, 17), 'Sheldon'),
        ((NAMES, 18), 'Sheldon'),
        ((NAMES, 19), 'Sheldon'),
        ((NAMES, 20), 'Leonard'),
        ((NAMES, 21), 'Leonard'),
        ((NAMES, 22), 'Leonard'),
        ((NAMES, 23), 'Leonard'),
        ((NAMES, 24), "Penny"),
        ((NAMES, 25), "Penny"),
        ((NAMES, 26), "Penny"),
        ((NAMES, 27), "Penny"),
        ((NAMES, 28), 'Rajesh'),
        ((NAMES, 29), 'Rajesh'),
        ((NAMES, 30), 'Rajesh'),
        ((NAMES, 31), 'Rajesh'),
        ((NAMES, 32), 'Howard'),
        ((NAMES, 33), 'Howard'),
        ((NAMES, 34), 'Howard'),
        ((NAMES, 35), 'Howard'),
        ((NAMES, 36), 'Sheldon'),
        ((NAMES, 37), 'Sheldon'),
        ((NAMES, 38), 'Sheldon'),
        ((NAMES, 39), 'Sheldon'),
        ((NAMES, 40), 'Sheldon'),
        ((NAMES, 41), 'Sheldon'),
        ((NAMES, 42), 'Sheldon'),
        ((NAMES, 43), 'Sheldon'),
        ((NAMES, 52), "Penny"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert whoIsNext(*args) == expected
