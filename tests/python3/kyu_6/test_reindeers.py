# pylint: disable=missing-docstring

"""How Many Reindeers?"""

import pytest

from python3.kyu_6.reindeers import reindeer

EXAMPLES = (
    ('presents', 'expected'),
    [
        (0, 2),
        (1, 3),
        (30, 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(presents, expected):
    assert reindeer(presents) == expected


def test_raise_error_if_too_high():
    with pytest.raises(ValueError):
        reindeer(200)
