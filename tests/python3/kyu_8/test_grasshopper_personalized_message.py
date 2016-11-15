# pylint: disable=missing-docstring

"""Grasshopper - Personalized Message"""

import pytest

from python3.kyu_8.grasshopper_personalized_message import greet

EXAMPLES = (
    ('name', 'owner', 'expected'),
    [
        ('Pavel', 'Pavel', 'Hello boss'),
        ('Greg', 'Pavel', 'Hello guest'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(name, owner, expected):
    assert greet(name, owner) == expected
