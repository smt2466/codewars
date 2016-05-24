"""Word a10n (abbreviation)
http://www.codewars.com/kata/5375f921003bf62192000746

The word i18n is a common abbreviation of internationalization the developer
community use instead of typing the whole word and trying to spell it
correctly. Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all words within that
string of length 4 or greater into an abbreviation following the same rules.

Notes:

  - A "word" is a sequence of alphabetical characters. By this definition,
    any other character like a space or hyphen (eg. "elephant-ride") will
    split up a series of letters into two words (eg. "elephant" and "ride").
  - The abbreviated version of the word should have the first letter, then
    the number of removed characters, then the last letter (eg. "e6t-r2e").
"""

import re

PATTERN = re.compile(r'(?:(\w+)(\W+)?)')


def abbreviate(text):
    """Cut too long words

    Args:
        text (str): Text to format

    Returns:
        str

    Examples:
        >>> abbreviate('hello the  awesome    world')
        'h3o the  a5e    w3d'
    """
    result = []
    for word, spacer in re.findall(PATTERN, text):
        if len(word) < 4:
            result.append(word)
        else:
            result.append(word[0] + str(len(word) - 2) + word[-1])
        result.append(spacer)
    return ''.join(result)
