"""Stop gninnipS My sdroW!
http://www.codewars.com/kata/5264d2b162488dc400000001

Write a function that takes in a string of one or more words, and returns the
same string, but with all five or more letter words reversed (Just like the
name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
"""


def spin_words(sentence):
    """Reverse all words in sentence shorter than 5 chars

    Args:
        sentence (str)

    Returns:
        str

    Examples:
        >>> spin_words('Hi world')
        'Hi dlrow'
    """
    return ' '.join(word if len(word) < 5 else word[::-1]
                    for word in sentence.split(' '))
