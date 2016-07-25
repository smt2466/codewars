"""Detect Pangram
https://www.codewars.com/kata/detect-pangram

A pangram is a sentence that contains every single letter of the alphabet at
least once. For example, the sentence "The quick brown fox jumps over the lazy
dog" is a pangram, because it uses the letters A-Z at least once (case is
irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is,
False if not. Ignore numbers and punctuation.
"""


from string import ascii_lowercase as alphabet


def is_pangram(text):
    """Checks if text is panagram"""
    return set(alphabet) == set(char for char in text.lower() if char.isalpha())
