"""Least Common Multiple
https://www.codewars.com/kata/least-common-multiple

Write a function that calculates the *least common multiple* of its arguments;
each argument is assumed to be a non-negative integer.
"""

from fractions import gcd


def lcm(*args):
    """Calculates least common multiple of arguments"""
    return reduce(lambda x, y: x*y/gcd(x, y), args)
