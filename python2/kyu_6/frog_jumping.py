"""Frog jumping
https://www.codewars.com/kata/536950ffc8a5ca9982001371

Help the frog to find a way to freedom

You have an array of integers and have a frog at the first position

    [Frog, int, int, int, ..., int]

The integer itself may tell you the length and the direction of the jump

     For instance:

      2 = jump two indices to the right
     -3 = jump three indices to the left
      0 = stay at the same position

Your objective is to find how many jumps are needed to jump out of the array.

Return -1 if Frog can't jump out of the array

    Example:
    array = [1, 2, 1, 5];
    jumps = 3  (1 -> 2 -> 5 -> <jump out>)
"""


def solution(array):
    """Finds number of frog jumps to leave the array

    Args:
        array (list): List of ints

    Returns:
        int: Number of jumps or -1 if impossible

    Examples:
        >>> solution([-3, 1, 2])
        1
        >>> solution([1, 2, 3])
        2
        >>> solution([2, 0, -2])
        -1
    """
    index, jumps = 0, 0
    seen = []
    while index not in seen:
        seen.append(index)
        try:
            index += array[index]
        except IndexError:
            return jumps
        jumps += 1
        if index < 0:
            return jumps
    return -1
