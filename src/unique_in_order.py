"""Unique In Order
http://www.codewars.com/kata/unique-in-order

Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each
other and preserving the original order of elements.
"""


def unique_in_order(seq):
    """Drop all elements whose are equal to previous

    Args:
        seq: Iterable object

    Returns:
        list

    Examples:
        >>> unique_in_order('aabbccd')
        ['a', 'b', 'c', 'd']
        >>> unique_in_order([1, 2, 3, 3, 3, 4])
        [1, 2, 3, 4]
    """
    result = [a for a, b in zip(seq[:-1], seq[1:]) if a != b]
    if seq:
        result.append(seq[-1])
    return result
