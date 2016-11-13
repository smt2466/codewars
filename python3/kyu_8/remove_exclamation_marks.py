"""Remove exclamation marks
https://www.codewars.com/kata/remove-exclamation-marks

Write function removeExclamationMarks which removes all exclamation marks from
a given string.
"""


def remove_exclamation_marks(strng: str) -> str:
    """Removes all exclamation marks"""
    return strng.replace('!', '')
