""""Does my number look big in this?
http://www.codewars.com/kata/5287e858c6b5a9678200083c

A Narcissistic Number is a number which is the sum of its own digits,
each raised to the power of the number of digits.

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634

The Challenge:

Your code must return true or false depending upon whether the given number
is a Narcissistic number.

Error checking for text strings or other invalid inputs is not required, only
valid integers will be passed into the function.
"""


def narcissistic(value):
    """Check if number if narcissistic

    Args:
        value (int): Number to check

    Returns:
        bool: Is narcissistic or not?

    Examples:
        >>> narcissistic(407)
        True
        >>> narcissistic(408)
        False
    """
    return sum(int(digit)**len(str(value)) for digit in str(value)) == value
