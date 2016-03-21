"""Build a pile of Cubes
http://www.codewars.com/kata/5592e3bd57b64d00f3000047

Your task is to construct a building which will be a pile of n cubes.
The cube at the bottom will have a volume of n^3, the cube above will have
volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find
the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb) will be an integer m
and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m
if such a n exists or -1 if there is no such n.

Examples:

    findNb(1071225) --> 45
    findNb(91716553919377) --> -1

Suggestion:

    Try to optimize your function.
"""

import decimal
from decimal import Decimal

decimal.getcontext().prec = 100


def find_nb(volume):
    """Find a number of cubes to fill the volume

    Args:
        volume (int)

    Returns:
        int: Number of cubes or -1

    Examples:
        >>> find_nb(1071225)
        45
        >>> find_nb(91716553919377)
        -1
    """
    pile = (-1 + Decimal(1 + 8*Decimal(volume).sqrt()).sqrt())/2
    return int(pile) if pile % 1 == 0 else -1
