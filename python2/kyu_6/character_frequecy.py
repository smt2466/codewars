"""Character frequency
https://www.codewars.com/kata/53e895e28f9e66a56900011a

Write a function that takes a piece of text in the form of a string and returns
the letter frequency count for the text. This count excludes numbers, spaces
and all punctuation marks. Upper and lower case versions of a character are
equivalent and the result should all be in lowercase.

The function should return a list of tuples (in Python) or arrays (in other
languages) sorted by the most frequent letters first. Letters with the same
frequency are ordered alphabetically. For example:

  letter_frequency('aaAabb dddDD hhcc')

will return

  [('d',5), ('a',4), ('b',2), ('c',2), ('h',2)]

Letter frequency analysis is often used to analyse simple substitution cipher
texts like those created by the Caesar cipher.
"""

from collections import Counter


def letter_frequency(text):
    """Count characters in string

    Args:
        text (str): Any text

    Returns:
        list: of tuples [(char, count), ...]

    Examples:
        >>> letter_frequency('aaabbc')
        [('a', 3), ('b', 2), ('c', 1)]
    """
    counter = Counter(text.lower())
    result = [(k, v) for k, v in counter.items() if k.isalpha()]
    return sorted(result, key=lambda x: (-x[1], x[0]))
