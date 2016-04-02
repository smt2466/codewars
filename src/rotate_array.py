"""Rotate Array (JS)
http://www.codewars.com/kata/rotate-array-js

Create a function named "rotate" that takes an array and returns a new one
with the elements inside rotated n spaces.

If n is greater than 0 it should rotate the array to the right. If n is less
than 0 it should rotate the array to the left. If n is 0, then it should
return the array unchanged.
"""


def rotate(array, shift):
    """Rotate an array with the given shift

    Args:
        array (list): List of any items
        shift (int): Shift (can be negative, positive or zero)

    Returns:
        list

    Examples:
        >>> rotate([1, 2, 3], 1)
        [3, 1, 2]
        >>> rotate([1, 2, 3], -1)
        [2, 3, 1]
        >>> rotate([1, 2, 3], 0)
        [1, 2, 3]
    """
    shift %= len(array)
    return array[-shift:] + array[:-shift]
