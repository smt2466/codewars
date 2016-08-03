# pylint: disable=missing-docstring

"""Modular Multiplicative Inverse"""

import pytest

from python3.kyu_6.modular_multiplicative_inverse import inverseMod

EXAMPLES = (
    ('args', 'expected'),
    [
        ([2, 5], 3),
        ([48, 101], 40),
        ([229, 105], 94)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert inverseMod(*args) == expected
