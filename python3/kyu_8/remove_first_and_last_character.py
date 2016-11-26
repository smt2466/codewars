"""Remove First and Last Character
https://www.codewars.com/kata/remove-first-and-last-character

It's pretty straightforward. Your goal is to create a function that removes
the first and last characters of a string. You're given one parameter.
"""


def remove_char(text):
    """Removes the first and latest characters from the given text

    Args:
        text (str): Text to process

    Returns:
        str: Given text without the first and latest characters

    Examples:
        >>> remove_char('hello world')
        'ello worl'
    """
    return text[1:-1]
