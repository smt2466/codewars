# pylint: disable=missing-docstring

"""Checking Groups"""

import pytest

from src.checking_groups import group_check

EXAMPLES = (
    ('groups', 'expected'),
    [
        ('()', True),
        ('({})', True),
        ('[[]()]', True),
        ('[{()}]', True),
        ('({', False),
        ('{(})', False),
        ('([]', False),
        ('[])', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(groups, expected):
    return group_check(groups) == expected
