# pylint: disable=missing-docstring

"""IPv4 to int32"""

import pytest

from python2.src.kyu_6.ipv4_to_int32 import ip_to_int32

EXAMPLES = (
    ('ipv4', 'expected'),
    [
        ('128.114.17.104', 2154959208),
        ('0.0.0.0', 0),
        ('48.208.31.197', 818945989),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(ipv4, expected):
    assert ip_to_int32(ipv4) == expected
