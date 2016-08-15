# pylint: disable=invalid-name, missing-docstring

"""House of cards"""

import pytest

from python3.kyu_6.house_of_cards import house_of_cards

EXAMPLES = (
    ('floors', 'expected'),
    [
        (1, 7),
        (2, 15),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(floors, expected):
    assert house_of_cards(floors) == expected


def test_raises_error_if_less_than_one_floor():
    with pytest.raises(ValueError):
        house_of_cards(0)
