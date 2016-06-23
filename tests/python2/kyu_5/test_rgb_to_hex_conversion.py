# pylint: disable=invalid-name, missing-docstring

"""RGB To Hex Conversion"""

import pytest

from python2.kyu_5.rgb_to_hex_conversion import to_hex, limit_code, rgb

CODE_TO_HEX = (
    ('int_code', 'hex_code'),
    [
        (255, 'FF'),
        (0, '00'),
        (148, '94'),
        (211, 'D3'),
    ]
)

COLOR_CODES = (
    ('code', 'expected'),
    [
        (-1, 0),
        (0, 0),
        (1, 1),
        (255, 255),
        (256, 255),
    ]
)

COLORS = (
    ('colors', 'expected'),
    [
        ([255, 255, 255], 'FFFFFF'),
        ([255, 255, 300], 'FFFFFF'),
        ([0, 0, 0], '000000'),
        ([148, 0, 211], '9400D3'),
    ]
)


@pytest.mark.parametrize(*COLOR_CODES)
def test_limit_code_returns_correct_result(code, expected):
    assert limit_code(code) == expected


@pytest.mark.parametrize(*CODE_TO_HEX)
def test_to_hex_returns_correct_result(int_code, hex_code):
    assert to_hex(int_code) == hex_code


@pytest.mark.parametrize(*COLORS)
def test_rgb_returns_correct_result(colors, expected):
    assert rgb(*colors) == expected
