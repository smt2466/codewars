"""Find The Parity Outlier
http://www.codewars.com/kata/find-the-parity-outlier

You are given an array (which will have a length of at least 3, but could be
very large) containing integers. The integers in the array are either entirely
odd or entirely even except for a single integer N. Write a method that takes
the array as an argument and returns N.

For example:

    [2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

    [160, 3, 1719, 19, 11, 13, -21]

Should return: 160
"""


def find_outlier(ints):
    """All integers are even or odd except one - find it

    Args:
        ints (list): List of integers

    Returns:
        int: Outlier

    Examples:
        >>> find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
        11
        >>> find_outlier([160, 3, 1719, 19, 11, 13, -21])
        160
    """
    rule = ints[0] % 2 == 0 and ints[1] % 2 == 0 or \
        ints[0] % 2 == 0 and ints[2] % 2 == 0 or \
        ints[1] % 2 == 0 and ints[2] % 2 == 0
    for item in ints:
        if item % 2 == rule:
            return item
