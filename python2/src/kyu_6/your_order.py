""""Your order, please
http://www.codewars.com/kata/55c45be3b2079eccff00010f

Your task is to sort a given string. Each word in the String will contain a
single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input
String will only contain valid consecutive numbers.
"""

import re

NUMBER = re.compile(r'.*(\d)+.*')


def get_number(word):
    """Extract digit from the word

    Args:
        word (str): String with one digit inside

    Returns:
        int: Integer from the given string

    Examples:
        >>> get_number('a1b')
        1
    """
    return int(re.match(NUMBER, word).group(1))


def order(text):
    """Sort words in sentence according to numbers inside them

    Args:
        text (str): Sentence with words having integer inside

    Returns:
        str: Sentence with sorted word order

    Examples:
        >>> order('a3 b1 c2')
        'b1 c2 a3'
        >>> order('')
        ''
    """
    return ' '.join(sorted(text.split(' '), key=get_number)) if text else ''

