"""WeIrD StRiNg CaSe
http://www.codewars.com/kata/52b757663a95b11b3d00062d

Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and
returns the same string with all even indexed characters in each word upper
cased, and all odd indexed characters in each word lower cased. The indexing
just explained is zero based, so the zero-ith index is even, therefore that
character should be upper cased.

The passed in string will only consist of alphabetical characters and
spaces(' '). Spaces will only be present if there are multiple words.
Words will be separated by a single space(' ').
"""


def to_weird(word):
    """Change string into weird style representation

    Args:
        word (str): Single word

    Returns:
        str

    Examples:
        >>> to_weird('hello')
        'HeLlO'
    """
    return ''.join(char.upper() if i % 2 == 0 else char
                   for i, char in enumerate(word))


def to_weird_case(string):
    """Change sentence into weird style representation

    Args:
        string (str): Sentence

    Returns:
        str

    Examples:
        >>> to_weird_case('hello world')
        'HeLlO WoRlD'
    """
    return ' '.join(to_weird(word) for word in string.split(' '))
