# pylint: disable=missing-docstring

"""Persistent Bugger."""

import pytest

from python2.kyu_6.persistent_bugger import persistence

EXAMPLES = (
    ('number', 'expected'),
    [
        (39, 3),
        (4, 0),
        (25, 2),
        (999, 4),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, expected):
    assert persistence(number) == expected
