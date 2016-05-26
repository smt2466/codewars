"""Replace With Alphabet Position
http://www.codewars.com/kata/546f922b54af40e1e90001da

Welcome. In this kata you are required to, given a string, replace every
letter with its position in the alphabet. If anything in the text isn't a
letter, ignore it and don't return it. a being 1, b being 2, etc.
"""

from string import ascii_lowercase as al


def alphabet_position(text):
    """Convert each alphabet char into corresponding alphaber position number

    Args:
        text (str): String to convert

    Returns:
        str

    Examples:
        >>> alphabet_position('Hello world')
        '8 5 12 12 15 23 15 18 12 4'
    """
    return ' '.join(str(ord(char) - 96) for char in text.lower() if char in al)
