# coding=utf-8

""""Look and say numbers
http://www.codewars.com/kata/53ea07c9247bc3fcaa00084d

There exists a sequence of numbers that follows the pattern

          1
         11
         21
        1211
       111221
       312211
      13112221
     1113213211
          .
          .
          .
Starting with "1" the following lines are produced by "saying what you see",
so that line two is "one one", line three is "two one(s)", line four is "one
two one one".

Write a function that given a starting value as a string, returns the
appropriate sequence as a list. The starting value can have any number of
digits. The termination condition is a defined by the maximum number of
iterations, also supplied as an argument.
"""

import re

PATTERN = re.compile(r'(.)\1*')


def say(number):
    """Say what you see

    Args:
        number (str): '1132'

    Returns:
        str: '211312'

    Examples:
        >>> say('11133455')
        '31231425'
    """
    sequences = [match.group() for match in PATTERN.finditer(number)]
    return ''.join(str(len(part)) + part[0] for part in sequences)


def look_and_say(data='1', maxlen=5):
    """Sequence of number mutations according to 'Say what you see' pattern

    Args:
        data (str): Start number
        maxlen (int): Number of mutation steps

    Returns:
        list: List of strings

    Examples:
        >>> look_and_say('12')
        ['1112', '3112', '132112', '1113122112', '311311222112']
    """
    result = []

    for _ in range(maxlen):
        data = say(data)
        result.append(data)

    return result
