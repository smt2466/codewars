# pylint: disable=missing-docstring

"""Calculate String Rotation"""

import pytest

from python2.kyu_6.string_rotation import shifted_diff

EXAMPLES = (
    ('first', 'second', 'expected'),
    [
        ("eecoff", "coffee", 4),
        ("Moose", "moose", -1),
        ("isn't", "'tisn", 2),
        ("Esham", "Esham", 0),
        (" ", " ", 0),
        ("hoop", "pooh", -1),
        ("  ", " ", -1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(first, second, expected):
    assert shifted_diff(first, second) == expected
