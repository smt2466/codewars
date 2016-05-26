"""Get All Possible Anagrams from a Hash
http://www.codewars.com/kata/543e926d38603441590021dd

Given a hash of letters and the number of times they occur, recreate all of
the possible anagram combinations that could be created using all of the
letters, sorted alphabetically.

The inputs will never include numbers, spaces or any special characters, only
lowercase letters a-z.
"""

from itertools import permutations


def get_words(hash_of_letters):
    """Compute all possible anagrams

    Args:
        hash_of_letters (dict): key - occurrence, value - letters

    Returns:
        list: List of possible anagrams (str)

    Examples:
        >>> get_words({1: ['a', 'b']})
        ['ab', 'ba']
    """
    letters = ''.join(''.join(k*letter for letter in letters)
                      for k, letters in hash_of_letters.items())
    return sorted(set(''.join(anagram) for anagram in permutations(letters)))
