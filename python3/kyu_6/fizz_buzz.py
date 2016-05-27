"""Fizz / Buzz
http://www.codewars.com/kata/51dda84f91f5b5608b0004cc

Write a function that takes an integer and returns an Array [A, B, C] where A
is the number of multiples of 3 (but not 5) less than the given integer, B is
the number of multiples of 5 (but not 3) less than the given integer and C is
the number of multiples of 3 and 5 less than the given integer.
"""


def solution(number):
    """Calculate number of multiples:

     - of 3 and not 5 less than number
     - of 5 and not 3 less than number
     - of 3 and 5 less than number

    Args:
        number (int)

    Returns:
        list: [<3_and_not_5>, <5_and_not_3>, <3_and_5>]

    Examples:
        >>> solution(21)
        [5, 3, 1]
    """
    number -= .5
    mul_3_not_5 = int(number//3 - number//15)
    mul_5_not_3 = int(number//5 - number//15)
    mul_3_and_5 = int(number//15)
    return [mul_3_not_5, mul_5_not_3, mul_3_and_5]

