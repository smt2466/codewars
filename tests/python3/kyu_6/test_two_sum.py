# pylint: disable=missing-docstring

"""Two Sum"""

import pytest

from python3.kyu_6.two_sum import two_sum

EXAMPLES = (
    ('numbers', 'target', 'expected'),
    [
        ([1, 2, 3], 4, [0, 2]),
        ([1234, 5678, 9012], 14690, [1, 2]),
        ([2, 2, 3], 4, [0, 1]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(numbers, target, expected):
    assert sorted(two_sum(numbers, target)) == expected
