# pylint: disable=redefined-builtin

"""Persistent Bugger
https://www.codewars.com/kata/persistent-bugger

Write a function, `persistence`, that takes in a positive parameter `num` and
returns its multiplicative persistence, which is the number of times you must
multiply the digits in `num` until you reach a single digit.
"""

from functools import reduce
from operator import mul


def persistence(number):
    """Finds number persistence"""
    result = 0
    while len(str(number)) != 1:
        number = reduce(mul, map(int, str(number)))
        result += 1
    return result
