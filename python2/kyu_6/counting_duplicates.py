"""Counting Duplicates
https://www.codewars.com/kata/counting-duplicates

### Count the number of Duplicates

Write a function that will return the count of *distinct* case-insensitive
alphabetic characters that occur more than once in the given string.
The given string can be assumed to contain only uppercase and lowercase
alphabets.
"""

from string import ascii_lowercase


def duplicate_count(text):
    """Count number of duplicated letters in text"""
    return sum(text.lower().count(char) > 1 for char in ascii_lowercase)
