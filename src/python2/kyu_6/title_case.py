"""Title Case
http://www.codewars.com/kata/5202ef17a402dd033c000009

A string is considered to be in title case if each word in the string is
either (a) capitalised (that is, only the first letter of the word is in
upper case) or (b) considered to be an exception and put entirely into lower
case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an
optional list of exceptions (minor words). The list of minor words will be
given as a string with each word separated by a space. Your function should
ignore the case of the minor words string -- it should behave in the same
way even if the case of the minor word string is changed.

Arguments

    First argument (required): the original string to be converted.
    Second argument (optional): space-delimited list of minor words that must
        always be lowercase except for the first word in the string.
        The JavaScript/CoffeeScript tests will pass undefined when this
        argument is unused.
"""


def title_case(title, minor_words=''):
    """Lowercase all minor words except first in title

    Args:
        title (str): Title to format
        minor_words (str): String of minor words

    Returns:
        str: Formatted title

    Examples:
        >>> title_case('hold on world', 'on')
        'Hold on World'
        >>> title_case('hello world')
        'Hello World'
    """
    result = []
    minor_words = [word.lower() for word in minor_words.split(' ')]
    for i, word in enumerate(title.split(' ')):
        if word.lower() not in minor_words or i == 0:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return ' '.join(result)
