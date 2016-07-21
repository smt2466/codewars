# pylint: disable=missing-docstring

"""Gray Code """

import pytest

from python2.kyu_6.gray_code import bin2gray, gray2bin

BIN2GRAY = (
    ('bits', 'expected'),
    [
        ([1, 0, 1], [1, 1, 1]),
        ([1, 1], [1, 0]),
    ]
)

GRAY2BIN = (
    ('bits', 'expected'),
    [
        ([1, 0], [1, 1]),
        ([1, 1, 1], [1, 0, 1]),
    ]
)


@pytest.mark.parametrize(*BIN2GRAY)
def test_bin2gray_returns_correct_result(bits, expected):
    assert bin2gray(bits) == expected


@pytest.mark.parametrize(*GRAY2BIN)
def test_gray2bin_returns_correct_result(bits, expected):
    assert gray2bin(bits) == expected
