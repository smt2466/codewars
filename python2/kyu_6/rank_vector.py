# coding=utf-8

""""Rank Vector
http://www.codewars.com/kata/545f05676b42a0a195000d95

Given an array (or list) of scores, return the array of ranks for each value
in the array. The largest value has rank 1, the second largest value has
rank 2, and so on. Ties should be handled by assigning the same rank to all
tied values. For example:

    ranks([9, 3, 6, 10]) = [2, 4, 3, 1]

and

    ranks([3, 3, 3, 3, 3, 5, 1]) = [2, 2, 2, 2, 2, 1, 7]

because there is one 1st place value, a five-way tie for 2nd place, and one
in 7th place.
"""


def ranks(scores):
    """Count ranks

    Args:
        scores (list): List of int scores

    Returns:
        list: Placement list of ints

    Examples:
        >>> ranks([5, 5, 2, 1, 3])
        [1, 1, 4, 5, 3]
    """
    i = 1
    placement = dict()

    for score in sorted(scores, reverse=True):
        if score not in placement:
            placement[score] = i
        i += 1

    return [placement[score] for score in scores]
