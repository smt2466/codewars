# pylint: disable=missing-docstring

"""IPv4 Parser"""

import pytest

from python2.kyu_6.ipv4_parser import ipv4__parser

EXAMPLES = (
    ('ip_addr', 'mask', 'network_block', 'host_identifier'),
    [
        ('192.168.50.1', '255.255.255.0', '192.168.50.0', '0.0.0.1'),
        ('192.168.50.129', '255.255.255.192', '192.168.50.128', '0.0.0.1'),
        ('65.196.188.53', '255.255.240.0', '65.196.176.0', '0.0.12.53')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(ip_addr, mask, network_block, host_identifier):
    assert ipv4__parser(ip_addr, mask) == (network_block, host_identifier)
