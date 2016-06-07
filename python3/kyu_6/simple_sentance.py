"""Simple Sentences
http://www.codewars.com/kata/5297bf69649be865e6000922

Implement a function, so it will produce a sentence out of the given parts.

Array of parts could contain:
- words;
- commas in the middle;
- multiple periods at the end.

Sentence making rules:
- there must always be a space between words;
- there must not be a space between a comma and word on the left;
- there must always be one and only one period at the end of a sentence.
"""

import re


def make_sentences(parts):
    """Construct sentence from parts

    Args:
        parts (list): List of strings (words and commas/dots

    Returns:
        str: Sentence with one dot at the end

    Examples:
        >>> make_sentences(['awesome', 'sentence'])
        'awesome sentence.'
    """
    result = ''
    for part in parts:
        if re.match(r'\w+', part):
            result += ' '
        result += part
    return result.lstrip().rstrip('.') + '.'
