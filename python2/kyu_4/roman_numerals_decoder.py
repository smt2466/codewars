"""Roman Numerals Decoder
https://www.codewars.com/kata/roman-numerals-decoder

Create a function that takes a Roman numeral as its argument and returns its
value as a numeric decimal integer. You don't need to validate the form of
the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the
number to be encoded separately, starting with the leftmost digit and skipping
any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is
rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666,
"MDCLXVI", uses each letter in descending order.
"""

ROMAN = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def solution(roman):
    """Convert Roman numerals to numeric decimal integer

    Args:
        roman (str): Roman number (ex. 'IX')

    Returns:
        int

    Examples:
        >>> solution('IX')
        9
    """
    result = 0
    i = 0
    while i < len(roman):
        if i == len(roman) - 1 or ROMAN[roman[i]] >= ROMAN[roman[i+1]]:
            result += ROMAN[roman[i]]
        else:
            result += ROMAN[roman[i+1]] - ROMAN[roman[i]]
            i += 1
        i += 1
    return result
