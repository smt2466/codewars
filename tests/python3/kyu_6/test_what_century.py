# pylint: disable=missing-docstring

"""What century is it?"""

import pytest

from python3.kyu_6.what_century import whatCentury

EXAMPLES = (
    ('year', 'expected'),
    [
        ('1999', '20th'),
        ('2011', '21st'),
        ('2154', '22nd'),
        ('2259', '23rd'),
        ('1124', '12th'),
        ('2000', '20th'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(year, expected):
    assert whatCentury(year) == expected
