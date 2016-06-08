# pylint: disable=missing-docstring

"""Does my number look big in this?"""

import pytest

from python2.kyu_6.narcissistic import narcissistic

EXAMPLES = (
    ('value', 'expected'),
    [
        (7, True),
        (371, True),
        (122, False),
        (4887, False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(value, expected):
    assert narcissistic(value) == expected
