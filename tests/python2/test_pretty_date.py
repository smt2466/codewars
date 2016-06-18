# pylint: disable=missing-docstring

"""Pretty date"""

import pytest

from python2.kyu_6.pretty_date import to_pretty

EXAMPLES = (
    ('seconds', 'expected'),
    [
        ('0', 'just now'),
        ('300', '5 minutes ago'),
        ('3600', 'an hour ago'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(seconds, expected):
    assert to_pretty(seconds) == expected
