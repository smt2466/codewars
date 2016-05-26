# coding=utf-8

"""Triangle type
http://www.codewars.com/kata/53907ac3cd51b69f790006c5

In this kata, you should calculate type of triangle with three given sides
a, b and c (given in any order).

If all angles are less than 90°, this triangle is acute and function should
return 1.

If one angle is strictly 90°, this triangle is right and function should
return 2.

If one angle more than 90°, this triangle is obtuse and function should
return 3.

If three sides cannot form triangle, or one angle is 180° (which turns
triangle into segment) - function should return 0.

Input parameters are sides of given triangle. All input values are
non-negative floating point or integer numbers (or both).
"""


def triangle_type(*args):
    """Check type of triangle

    0 : if triangle cannot be made with given sides
    1 : acute triangle
    2 : right triangle
    3 : obtuse triangle

    Args:
        *args: Sides (int)

    Returns:
        int: Triangle type

    Examples:
        >>> triangle_type(21, 220, 221)
        2
    """
    longest = max(args)
    shortest = min(args)
    square_sum = shortest**2 + (sum(args) - shortest - longest)**2

    if 2*longest >= sum(args):      # Is triangle?
        return 0
    elif square_sum > longest**2:   # Is acute
        return 1
    elif square_sum == longest**2:  # Is right?
        return 2
    else:                           # Is obtuse?
        return 3
