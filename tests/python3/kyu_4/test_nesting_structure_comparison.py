# pylint: disable=missing-docstring

"""Nesting Structure Comparison"""

import pytest

from python3.kyu_4.nesting_structure_comparison import same_structure_as


EXAMPLES = (
    ('original', 'other', 'expected'),
    [
        ([1, 1, 1], [2, 2, 2], True),
        ([1, [1, 1]], [2, [2, 2]], True),
        ([1, [1, 1]], [[2, 2], 2], False),
        ([1, [1, 1]], [[2], 2], False),
        ([[[], []]], [[[], []]], True),
        ([[[], []]], [[1, 1]], False),
        ([1, [1, 1]], [2, [2]], False),
        ([], {}, False),
        ([1, '[', ']'], ['[', ']', 1], True)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(original, other, expected):
    assert same_structure_as(original, other) == expected
