# pylint: disable=missing-docstring

"""Convert string to camel case"""

import pytest

from python3.kyu_5.convert_string_to_camel_case import to_camel_case


EXAMPLES = (
    ('text', 'expected'),
    [
        ('', ''),
        ('the_stealth_warrior', 'theStealthWarrior'),
        ('The-Stealth-Warrior', 'TheStealthWarrior'),
        ('A-B-C', 'ABC'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert to_camel_case(text) == expected
