"""IPv4 Parser
http://www.codewars.com/kata/ipv4-parser

Write a function that takes two string parameters, an IP (v4) address and
a subnet mask, and returns two strings: the network block, and the host
identifier.

The function does not need to support CIDR notation.

Description

A single IP address with subnet mask actually specifies several addresses:
a network block, and a host identifier, and a broadcast address. These
addresses can be calculated using a bitwise AND operation on each bit.

(The broadcast address is not used in this kata.)
"""


def ipv4__parser(ip_addr, mask):
    """Find network block and host identifier given ip address and mask

    Args:
        ip_addr (str): IPv4 adress
        mask (str): Network mask

    Returns:
        tuple: (network block, host identifier)

    Examples:
        >>> ipv4__parser('192.168.2.1', '255.255.255.0')
        ('192.168.2.0', '0.0.0.1')
    """
    ip_addr = [int(octet) for octet in ip_addr.split('.')]
    mask = [int(octet) for octet in mask.split('.')]
    net_addr = [str(ip_octet & mask_octet)
                for (ip_octet, mask_octet) in zip(ip_addr, mask)]
    host_addr = [str(ip_octet & ~comp_octet)
                 for (ip_octet, comp_octet) in zip(ip_addr, mask)]
    return '.'.join(net_addr), '.'.join(host_addr)
