# coding=utf-8

"""Next Featured Number Higher than a Given Value
http://www.codewars.com/kata/next-featured-number-higher-than-a-given-value

Make a function that receives a value, val and outputs the smallest higher
number than the given value, and this number belong to a set of positive
integers that have the following properties:

 - their digits occur only once
 - they are odd
 - they are multiple of three

    next_numb(12) == 15
    next_numb(13) == 15
    next_numb(99) == 105
    next_numb(999999) == 1023459
    next_number(9999999999) == "There is no possible number that
    fulfills those requirements"
"""


def next_numb(val):
    """Find nearest integer according to rules

    - their digits occur only once
    - they are odd
    - they are multiple of three

    Args:
        val (int): Base integer

    Returns:
        int or str: Nearest number or error message if impossible to find

    Examples:
        >>> next_numb(99)
        105
    """
    val += 1
    if val >= 9876543210:
        return "There is no possible number that fulfills those requirements"

    while not (val % 2 != 0 and
               val % 3 == 0 and
               len(set(str(val))) == len(str(val))):
        val += 1
    return val
