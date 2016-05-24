""""Duplicate Encoder
http://www.codewars.com/kata/54b42f9314d9229fd6000d9c

The goal of this exercise is to convert a string to a new string where each
character in the new string is '(' if that character appears only once in the
original string, or ')' if that character appears more than once in the
original string. Ignore capitalization when determining if a character
is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("
"""

from collections import Counter


def duplicate_encode(word):
    """Replace all duplicated chars by ) else (

    Args:
        word (str)

    Returns:
        str: Sequence of ()

    Examples:
        >>> duplicate_encode('Hello world')
        '(()))(()()('
    """
    word = word.lower()
    counter = Counter(word)
    return ''.join('(' if counter[char] == 1 else ')' for char in word)
