# coding=utf-8

"""Rotate for a Max
http://www.codewars.com/kata/rotate-for-a-max

Take a number: 56789. Rotate left, you get 67895.

Keep the first digit in place and rotate left the other digits: 68957.

Keep the first two digits in place and rotate the other ones: 68579.

Keep the first three digits and rotate left the rest: 68597. Now it is over
since keeping the first four it remains only one digit which rotated is itself.

You have the following sequence of numbers:

56789 -> 67895 -> 68957 -> 68579 -> 68597

and you must return the greatest: 68957.

Calling this function max_rot (or maxRot or ... depending on the language)

max_rot(56789) should return 68957
"""


def max_rot(number):
    """Rotate number to find max

    Args:
        number (int): Initial number

    Returns:
        int: Result number

    Examples:
        >>> max_rot(56789)
        68957
    """
    i = 0
    history = [number]
    number = str(number)
    while i != len(number) - 1:
        number = number[:i] + number[i + 1:] + number[i]
        history.append(int(number))
        i += 1
    return max(history)
