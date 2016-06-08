# pylint: disable=missing-docstring

"""Good vs Evil"""

import pytest

from python2.kyu_6.good_vs_evil import goodVsEvil, GOOD_WINS, EVIL_WINS, TIE

EXAMPLES = (
    ('good', 'evil', 'expected'),
    [
        ('1 1 1 1 1 1', '1 1 1 1 1 1 1', EVIL_WINS),
        ('0 0 0 0 0 10', '0 1 1 1 1 0 0', GOOD_WINS),
        ('1 0 0 0 0 0', '1 0 0 0 0 0 0', TIE),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(good, evil, expected):
    assert goodVsEvil(good, evil) == expected
