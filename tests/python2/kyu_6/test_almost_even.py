# pylint: disable=missing-docstring

"""Almost Even"""

import pytest

from python2.kyu_6.almost_even import splitInteger

EXAMPLES = (
    ('num', 'parts', 'expected'),
    [
        (10, 1, [10]),
        (2, 2, [1, 1]),
        (20, 5, [4, 4, 4, 4, 4]),
        (20, 6, [3, 3, 3, 3, 4, 4])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, parts, expected):
    assert splitInteger(num, parts) == expected
