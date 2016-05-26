# pylint: disable=invalid-name

"""Reversed Words
http://www.codewars.com/kata/51c8991dee245d7ddf00000e

Complete the solution so that it reverses all of the words within the string
passed in.
"""


def reverseWords(line):
    """Reverse words in line

    Args:
        line (str): String of words

    Returns:
        str: Line with reversed word order

    Examples:
        >>> reverseWords('John Doe')
        'Doe John'
    """
    return ' '.join(line.split()[::-1])
