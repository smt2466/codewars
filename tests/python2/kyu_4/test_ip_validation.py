# pylint: disable=missing-docstring

"""IP Validation"""

import pytest

from python2.kyu_4.ip_validation import is_valid_IP


EXAMPLES = (
    ('ipv4', 'expected'),
    [
        ('1.2.3.4', True),
        ('123.45.67.89', True),
        ('1.2.3', False),
        ('1.2.3.4.5', False),
        ('123.456.78.90', False),
        ('123.045.067.089', False),
        ('12.255.56.1', True),
        ('', False),
        ('abc.def.ghi.jkl', False),
        ('123.456.789.0', False),
        ('12.34.56', False),
        ('12.34.56 .1', False),
        ('12.34.56.-1', False),
        ('123.045.067.089', False),
        ('256.1.2.3', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(ipv4, expected):
    assert is_valid_IP(ipv4) == expected
