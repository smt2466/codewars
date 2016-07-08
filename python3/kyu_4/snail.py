"""Snail
https://www.codewars.com/kata/snail

Given an `n x n` array, return the array elements arranged from outermost
elements to the middle element, traveling clockwise.

NOTE: The idea is not sort the elements from the lowest value to the highest;
the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as ``[[]]``
"""

import math


def snail(array):
    """Snail-sort matrix elements"""
    side = len(array)
    result = []

    for i in range(math.ceil(len(array)/2)):
        result += array[i][i:side-i]                             # Top
        result += [row[side-i-1] for row in array[i+1:side-i]]   # Left
        result += array[side-i-1][i:side-i-1][::-1]              # Bottom
        result += [row[i] for row in array[i+1:side-i-1][::-1]]  # Right

    return result
