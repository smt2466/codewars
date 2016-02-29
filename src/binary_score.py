# coding=utf-8

"""Binary scORe
http://www.codewars.com/kata/56cafdabc8cfcc3ad4000a2b

Given a number n we will define it's scORe to be 0 | 1 | 2 | 3 | ... | n,
where | is the bitwise OR operator.

Write a function that takes n and finds it's scORe.
"""


def score(num):
    """Num reduce by binary OR

    Args:
        num (int)

    Returns:
        int

    Examples:
        >>> score(17204)
        32767
    """
    return int(bin(num)[2:].replace('0', '1'), 2) if num else 0
