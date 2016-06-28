"""Largest 5 digit number in a series
https://www.codewars.com/kata/largest-5-digit-number-in-a-series

In the following 6 digit number:
    283910

91 is the greatest sequence of 2 digits.

Complete the solution so that it returns the largest five digit number found
within the number given. The number will be passed in as a string of only
digits. It should return a five digit integer. The number passed may be as
large as 1000 digits.
"""


def solution(digits):
    """Find the biggest 5-digit number in given digit sequence

    Args:
        digits (str): Digit sequence

    Returns:
        int: Biggest 5-digit number

    Examples:
        >>> solution('123454321')
        54321
    """
    biggest = [0]*5
    for i, _ in enumerate(digits[:-4]):
        prev = False
        for j in range(5):
            if prev or int(digits[i+j]) >= biggest[j]:
                if int(digits[i+j]) > biggest[j]:
                    prev = True
                biggest[j] = int(digits[i + j])
            else:
                break
    return int(''.join(str(x) for x in biggest))
