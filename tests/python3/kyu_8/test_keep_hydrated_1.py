# pylint: disable=missing-docstring

"""Keep Hydrated!"""

import pytest

from python3.kyu_8.keep_hydrated_1 import litres

EXAMPLES = (
    ('time', 'expected'),
    [
        (2, 1),
        (1.4, 0),
        (12.3, 6),
        (0.82, 0),
        (11.8, 5),
        (1787, 893),
        (0, 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(time, expected):
    assert litres(time) == expected
