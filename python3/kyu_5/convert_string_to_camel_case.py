"""Convert string to camel case
https://www.codewars.com/kata/convert-string-to-camel-case

Complete the method/function so that it converts dash/underscore delimited
words into camel casing. The first word within the output should be capitalized
only if the original word was capitalized.
"""

import re


def to_camel_case(text):
    """Converts text to camel case

    Args:
        text (str): Text to camel case

    Returns:
        str: Camel case text

    Examples:
        >>> to_camel_case('hello_world')
        'helloWorld'
    """
    try:
        words = re.split(r'[^a-zA-Z]', text)
        first = words[0]
        first = first.capitalize() if first[0].isupper() else first.lower()
        return first + ''.join(word.capitalize() for word in words[1:])
    except IndexError:
        return ''
