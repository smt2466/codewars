"""Consecutive strings
http://www.codewars.com/kata/consecutive-strings

You are given an array strarr of strings and an integer k. Your task is to
return the first longest string consisting of k consecutive strings taken
in the array.

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
"""


def longest_consec(strarr, num):
    """Find longest consecutive string

    Args:
        strarr (list): List of strings
        num (int): Number of consecutive strings to found

    Returns:
        str

    Examples:
        >>> longest_consec(['a', 'bc', 'def'], 2)
        'bcdef'
    """
    if not strarr or num < 1 or num > len(strarr):
        return ''

    longest = 0
    longest_i = None

    for i in range(len(strarr)):
        length = sum(len(item) for item in strarr[i:i + num])
        if length > longest:
            longest = length
            longest_i = i

    return ''.join(strarr[longest_i:longest_i + num])
