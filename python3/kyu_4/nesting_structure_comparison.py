"""Nesting Structure Comparison
https://www.codewars.com/kata/nesting-structure-comparison

Complete the method (or function in Python) to return true when its argument is
an array that has the same nesting structure as the first array.
"""

from collections import Iterable


def not_collection(obj):
    """Check if obj is a collection but not a string"""
    return isinstance(obj, str) or not isinstance(obj, Iterable)


def same_structure_as(original, other):
    """Compare structures of original and other objects (but not values)"""
    if not_collection(original) and not_collection(other):
        return True
    if not isinstance(original, type(other)) or len(original) != len(other):
        return False
    return all(same_structure_as(x, y) for x, y in zip(original, other))
