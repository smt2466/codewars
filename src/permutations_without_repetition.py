# pylint: disable=redefined-builtin

"""Number of permutations without repetitions
http://www.codewars.com/kata/571bff6082661c8a11000823

Write a function that takes a number or a string and gives back the number
of permutations without repetitions that can generated using all its element

For example, starting with:

    1
    45
    115
    "abc"

You could respectively generate:

    1
    45,54
    115,151,511
    "abc","acb","bac","bca","cab","cba"

So you should have, in turn:

    perms(1)==1
    perms(45)==2
    perms(115)==3
    perms("abc")==6
"""

from functools import reduce
from math import factorial
from operator import mul


def perms(element):
    """Find the number of permutations of items without repetitions

    Args:
        element (int or str): Collections of items

    Returns:
        int: Number of permutations without repetitions

    Examples:
        >>> perms(112233)
        90
        >>> perms('aabbcc')
        90
    """
    element = str(element)
    items = len(element)
    reps = [factorial(element.count(char)) for char in set(element)]
    return factorial(items)/reduce(mul, reps)
