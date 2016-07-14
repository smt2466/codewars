# pylint: disable=missing-docstring

"""Pete, the baker"""

import pytest

from python2.kyu_5.pete_the_baker import cakes


EXAMPLES = (
    ('recipe', 'available', 'expected'),
    [
        ({'flour': 500, 'sugar': 200, 'eggs': 1},
         {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200},
         2),
        ({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},
         {'sugar': 500, 'flour': 2000, 'milk': 2000},
         0)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(recipe, available, expected):
    assert cakes(recipe, available) == expected
