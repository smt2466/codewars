"""Where my anagrams at?
https://www.codewars.com/kata/where-my-anagrams-at

What is an anagram? Well, two words are anagrams of each other if they both
contain the same letters.

Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words. You should
return an array of all the anagrams or an empty array if there are none.
"""

from collections import Counter


def anagrams(goal, words):
    """Find all anagrams of the word in the given array

    Args:
        goal (str): Word to search anagrams
        words (list): Array of words to search for anagrams

    Returns:
        list: All goal anagrams in the words array

    Examples:
        >>> anagrams('word', ['rowd', 'orwd', 'abce'])
        ['rowd', 'orwd']
    """
    return [word for word in words if Counter(word) == Counter(goal)]
