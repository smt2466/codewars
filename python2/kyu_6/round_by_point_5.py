"""Round by 0.5 steps
http://www.codewars.com/kata/51f1342c76b586046800002a

Round any given number to the closest 0.5 step
"""

import math


def solution(num):
    """Round to the nearest .5 number

    Args:
        num (float): Number to round

    Returns:
        int or float

    Examples:
        >>> solution(4.3)
        4.5
    """
    result = math.floor(num)
    if num % 1 >= .75:
        result += 1
    elif num % 1 >= .25:
        result += .5
    return result
