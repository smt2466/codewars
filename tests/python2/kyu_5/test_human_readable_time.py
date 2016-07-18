# pylint: disable=missing-docstring

"""Human Readable Time"""

import pytest

from python2.kyu_5.human_readable_time import make_readable

EXAMPLES = (
    ('seconds', 'expected'),
    [
        (0, '00:00:00'),
        (5, '00:00:05'),
        (60, '00:01:00'),
        (86399, '23:59:59'),
        (359999, '99:59:59'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(seconds, expected):
    assert make_readable(seconds) == expected
