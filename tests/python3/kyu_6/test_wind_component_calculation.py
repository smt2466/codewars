# pylint: disable=missing-docstring

"""Wind component calculation"""

import pytest

from python3.kyu_6.wind_component_calculation import wind_info

EXAMPLES = (
    ('runway', 'wind_direction', 'wind_speed', 'expected'),
    [
        ('18', 170, 15,
         'Headwind 15 knots. Crosswind 3 knots from your left.'),
        ('18', 210, 14,
         'Headwind 12 knots. Crosswind 7 knots from your right.'),
        ('22L', 160, 14,
         'Headwind 7 knots. Crosswind 12 knots from your left.'),
        ('18', 70, 15,
         'Tailwind 5 knots. Crosswind 14 knots from your left.'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(runway, wind_direction, wind_speed, expected):
    assert wind_info(runway, wind_direction, wind_speed) == expected
