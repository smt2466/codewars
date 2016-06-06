# pylint: disable=invalid-name

""""Find the Mine!
http://www.codewars.com/kata/528d9adf0e03778b9e00067e

You've just discovered a square (NxN) field and you notice a warning sign.
The sign states that there's a single bomb in the 2D grid-like field in front
of you.

Write a function mineLocation that accepts a 2D array, and returns the location
of the mine. The mine is represented as the integer 1 in the 2D array. Areas in
the 2D array that are not the mine will be represented as 0s.

The location returned should be an array where the first element is the row
index, and the second element is the column index of the bomb location (both
should be 0 based). All 2D arrays passed into your function will be square
(NxN), and there will only be one mine in the array.
"""


def mineLocation(field):
    """Find mine coordinates

    Args:
        field (list): 2D array of zeroes, mine is 1

    Returns:
        list: Mine coordinates

    Examples:
        >>> mineLocation([[0, 0], [1, 0]])
        [1, 0]
    """
    for i, row in enumerate(field):
        for j, mine in enumerate(row):
            if mine:
                return [i, j]
