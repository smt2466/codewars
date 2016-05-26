# coding=utf-8

"""Exercise in Summing
http://www.codewars.com/kata/exercise-in-summing

Your task is to finish two functions, minimumSum and maximumSum, that take 2
parameters:

    - values: an array of integers with an arbitrary length; may be positive
      and negative
    - n: how many integers should be summed; always 0 or bigger

Example:

    values = [5, 4, 3, 2, 1];
    minimum_sum(values, 2) #should return 1 + 2 = 3
    maximum_sum(values, 3) #should return 3 + 4 + 5 = 12

All values given to the functions will be integers. Also take care of the
following special cases:

    - if values is empty, both functions should return 0
    - if n is 0, both functions should also return 0
    - if n is larger than values's length, use the length instead.
"""


def sum_few(values, num, reverse):
    """Sum first num items of sorted values array

    Args:
        values (list): List of ints
        num (int): Number of items to sum
        reverse (bool): How to order an array

    Returns:
        int

    Examples:
        >>> sum_few([1, 2, 3], 2, True)
        5
        >>> sum_few([1, 2, 3], 2, False)
        3
    """
    return sum(sorted(values, reverse=reverse)[:num])


def minimum_sum(values, num):
    """Sum the num smallest integers in the array values

    Args:
        values (list): List of ints to sum
        num (int): Number of items to sum

    Returns:
        int: Summary

    Examples:
        >>> minimum_sum([9, 1, 8, 2], 2)
        3
    """
    return sum_few(values, num, reverse=False)


def maximum_sum(values, num):
    """Sum the num largest integers in the array values

    Args:
        values (list): List of ints to sum
        num (int): Number of items to sum

    Returns:
        int: Summary

    Examples:
        >>> maximum_sum([9, 1, 8, 2], 2)
        17
    """
    return sum_few(values, num, reverse=True)
