"""Simple Pig Latin
https://www.codewars.com/kata/simple-pig-latin

Move the first letter of each word to the end of it, then add 'ay' to the end
of the word.
"""


def pig_it(text: str) -> str:
    """Convert text into Pig Latin

    Examples:
        >>> pig_it('Hello world')
        'elloHay orldway'
    """
    result = []
    words = text.split()
    for word in words:
        if word.isalpha():
            result.append(word[1:] + word[0] + 'ay')
        else:
            result.append(word)
    return ' '.join(result)
