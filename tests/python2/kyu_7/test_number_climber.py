# pylint: disable=missing-docstring

"""Number Climber"""

import pytest

from python2.kyu_7.number_climber import climb

EXAMPLES = (
    ('number', 'sequence'),
    [
        (13, [1, 3, 6, 13]),
        (10, [1, 2, 5, 10]),
        (1, [1]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, sequence):
    assert climb(number) == sequence
