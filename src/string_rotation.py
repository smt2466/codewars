"""Calculate String Rotation
http://www.codewars.com/kata/calculate-string-rotation

The goal of this exercise is to write a method that takes two strings as
parameters and returns an integer n, where n is equal to the amount of spaces
"rotated forward" the second string is relative to the first string (more
precisely, to the first character of the first string).

For instance, take the strings "fatigue" and "tiguefa". In this case, the first
string has been rotated 5 characters forward to produce the second string, so 5
would be returned.

If the second string isn't a valid rotation of the first string, the method
returns -1.
"""


def shifted_diff(first, second):
    """Find number of shifts to mutate first string into second

    Args:
        first (str): String to be shifted
        second (str): String to achieve

    Returns:
        int: Number of shifts if possible or -1

    Examples:
        >>> shifted_diff('llohe', 'hello')
        2
        >>> shifted_diff('helloworld', 'hello')
        -1
    """
    for i in range(len(first)):
        if first[-i:] + first[:-i] == second:
            return i
    return -1
