"""Triple trouble
http://www.codewars.com/kata/55d5434f269c0c3f1b000058

Write a function triple_double(num1, num2) which takes in numbers num1 and
num2 and returns 1 if there is a straight triple of a number at any place
in num1 and also a straight double of the same number in num2.

If this isn't the case, return 0
"""


def triple_double(num1, num2):
    """Check if there straight triple in num1 and straight double in num2

    Args:
        num1 (int): Where to find straight triple
        num2 (int): Where to find straight double

    Returns:
        int: 1 or 0

    Examples:
        >>> triple_double(123444, 9044)
        1
    """
    for i in range(10):
        if str(i)*3 in str(num1) and str(i)*2 in str(num2):
            return 1
    return 0
