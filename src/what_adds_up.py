# coding=utf-8
# pylint: disable=invalid-name

""""What adds up
http://www.codewars.com/kata/53cce49fdf221844de0004bd

Given three arrays of integers your task is to create an algorithm that finds
the numbers in the first two arrays whose sum is equal to any number in the
third. The return value should be an array containing the values from the
argument arrays that adds up. The sort order of the resulting array is not
important. If no combination of numbers adds up return a empty array.
"""


def addsup(a1, a2, a3):
    """Find two numbers from a1 and a3 that their sum is in a3

    Args:
        a1 (list)
        a2 (list)
        a3 (list)

    Returns:
        list: [int_from_a1, int_from_a2, their_sum_from_a3]

    Examples:
        >>> addsup([1, 2], [4, 3], [6, 5, 8])
        [[1, 4, 5], [2, 4, 6], [2, 3, 5]]
    """
    return [[a1_el, a2_el, a1_el + a2_el] for a1_el in a1 for a2_el in a2
            if a1_el + a2_el in a3]
