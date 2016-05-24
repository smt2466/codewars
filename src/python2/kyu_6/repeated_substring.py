# coding=utf-8
# pylint: disable=invalid-name

"""Repeated Substring
http://www.codewars.com/kata/5491689aff74b9b292000334

For a given nonempty string s find a minimum substring t and the maximum
number k, such that the entire string s is equal to t repeated k times.
The input string consists of lowercase latin letters. Your function should
return a tuple (in Python) (t, k) or an array (in Ruby and JavaScript) [t, k]

Example #1:

    for string

        s = "ababab"

    the answer is

        ("ab", 3)

Example #2:

    for string

        s = "abcde"

    the answer is

        ("abcde", 1)
        ["abcde", 1]

because for this string "abcde" the minimum substring t, such that s is t
repeated k times, is itself.
"""


def f(s):
    """Find if s composes of one repeated substring

    Args:
        s (str): String to find substring

    Returns:
        tuple(str, int): Composite substring and number of occurrence

    Examples:
        >>> f('strstrstr')
        ('str', 3)
    """
    for i in range(1, len(s) + 1):
        substring = s[:i]
        occurrence = s.count(substring)
        if substring*occurrence == s:
            return substring, occurrence
