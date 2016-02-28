# coding=utf-8

""""Zip it!
http://www.codewars.com/kata/56aaf25213edd3a88a000002/train/python

Write lstzip function that merges the corresponding elements of two sequences
using a specified selector function fn (a block in Ruby)

For example:

    a = [1, 2, 3, 4, 5]
    b = ['a', 'b']
    lstzip(a,b, lambda a,b: str(a)+str(b))

    a = [1, 2, 3, 4, 5]
    b = ['a','b','c','d','e']
    lstzip(a,b, lambda a, b: a * ord(b[0]))

if arrays have different lengths, go up to the minimum length and then stop.
"""


def lstzip(list1, list2, func):
    """Merge two lists

    Args:
        list1 (list): List to zip
        list2 (list): List to zip
        func: Zip function

    Returns:
        list: Product if zip

    Examples:
        >>> a = [1, 2, 3, 4, 5]
        >>> b = ['a', 'b']
        >>> lstzip(a, b, lambda a, b: str(a) + str(b))
        ['1a', '2b']
        >>> a = [1, 2, 3, 4, 5]
        >>> b = ['a','b','c','d','e']
        >>> lstzip(a, b, lambda a, b: a * ord(b[0]))
        [97, 196, 297, 400, 505]
    """
    return [func(x, y) for x, y in zip(list1, list2)]
