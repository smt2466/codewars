# pylint: disable=invalid-name

"""IP Validation
https://www.codewars.com/kata/ip-validation

Write an algorithm that will identify valid IPv4 addresses in dot-decimal
format. Input to the function is guaranteed to be a single string.
"""

import re

IP_PATTERN = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')


def is_valid_IP(ipv4):
    """Check if IPv4 is valid

    Args:
        ipv4 (str): IP address

    Returns:
        bool: Valid or not

    Examples:
        >>> is_valid_IP('8.8.8.8')
        True
    """
    match = re.match(IP_PATTERN, ipv4)
    if not match:
        return False
    parts = match.groups()

    for part in parts:
        if int(part) < 0 or int(part) > 255:
            return False
        if part.startswith('0') and len(part) > 1:
            return False
    return True
