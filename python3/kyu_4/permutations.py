"""Permutations
https://www.codewars.com/kata/permutations

In this kata you have to create all permutations of an input string and remove
duplicates, if present. This means, you have to shuffle all letters from the
input in all possible orders.

The order of the permutations doesn't matter.
"""

import itertools

from typing import List


def permutations(string: str) -> List[str]:
    """Returns all string permutations"""
    perms = sorted(set(itertools.permutations(string)))
    return list(''.join(perm) for perm in perms)
