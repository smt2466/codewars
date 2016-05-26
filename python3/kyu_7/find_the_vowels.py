"""Find the vowels
http://www.codewars.com/kata/5680781b6b7c2be860000036

We want to know the index of the vowels in a given word, for example, there are
two vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

NOTE: Vowels in this context refers to English Language Vowels - a e i o u y

NOTE: this is indexed from [1..n] (not zero indexed!)
"""

VOWELS = 'aeiouy'


def vowel_indices(word):
    """Return list of vowels indexes based 1

    Args:
        word (str)

    Returns:
        list: List of integer indexes based 1

    Examples:
        >>> vowel_indices('awesome')
        [1, 3, 5, 7]
    """
    return [i + 1 for (i, char) in enumerate(word) if char.lower() in VOWELS]
