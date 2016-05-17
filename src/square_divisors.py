"""Integers: Recreation One
http://www.codewars.com/kata/55aa075506463dac6600010d

Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are:
1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which
is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m
and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays, each subarray having two elements,
first the number whose squared divisors is a square and then the sum of the
squared divisors.
"""

import math
from itertools import chain


def list_squared(start, stop):
    """Find all numbers between start and stop which sum of squares of
     divisors is a square

    Args:
        start (int): Start of the number search range
        stop (int): End of the number search range

    Returns:
        list: [[number, sum_of_squares], ...]

    Examples:
        >>> list_squared(1, 43)
        [[1, 1], [42, 2500]]
    """
    result = []

    for num in range(start, stop):
        divisors = set(chain.from_iterable((
            [i, num/i] for i in range(1, int(math.sqrt(num)) + 1)
            if num % i == 0
        )))
        divisor_squares = [x*x for x in divisors]
        divisor_squares_sum = sum(divisor_squares)
        if math.sqrt(divisor_squares_sum).is_integer():
            result.append([num, divisor_squares_sum])

    return result
