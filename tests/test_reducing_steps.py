# pylint: disable=missing-docstring

"""Reducing by steps"""

import pytest

from src.reducing_by_steps import (
    gcdi, lcmu, som, maxi, mini, oper_array
)


EXAMPLES = (
    ('fct', 'arr', 'init', 'expected'),
    [
        (gcdi, [18, 69, -90, -78, 65, 40], 18,
         [18, 3, 3, 3, 1, 1]),
        (lcmu, [18, 69, -90, -78, 65, 40], 18,
         [18, 414, 2070, 26910, 26910, 107640]),
        (som, [18, 69, -90, -78, 65, 40], 0,
         [18, 87, -3, -81, -16, 24]),
        (mini, [18, 69, -90, -78, 65, 40], 18,
         [18, 18, -90, -90, -90, -90]),
        (maxi, [18, 69, -90, -78, 65, 40], 18,
         [18, 69, 69, 69, 69, 69])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(fct, arr, init, expected):
    assert oper_array(fct, arr, init) == expected
