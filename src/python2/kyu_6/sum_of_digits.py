"""Sum of Digits / Digital Root
http://www.codewars.com/kata/541c8630095125aba6000c00

In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n,
take the sum of the digits of n. If that value has two digits, continue
reducing in this way until a single-digit number is produced. This is only
applicable to the natural numbers.
"""


def digital_root(number):
    """Sum all digits of number until one digit number remains

    Args:
        number (int): Number to sum

    Returns:
        int: Single digit number

    Examples:
        >>> digital_root(123)
        6
    """
    if number < 10:
        return number
    else:
        return digital_root(sum(int(digit) for digit in str(number)))
