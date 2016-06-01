"""Sequences and Series
http://www.codewars.com/kata/5254bd1357d59fbbe90001ec

Have a look at the following numbers.

     n | score
    ---+-------
     1 |  50
     2 |  150
     3 |  300
     4 |  500
     5 |  750

Can you find a pattern in it? If so, then write a function getScore(n) which
returns the score for any positive number n:

    get_score(1) #=> == 50
    get_score(2) #=> == 150
    get_score(3) #=> == 300
"""


def get_score(num):
    """Find nth-number in sequence

    Args:
        num (int)

    Returns:
        int: nth-number in sequence

    Examples:
        >>> get_score(10)
        2750
    """
    return 25*num*(num + 1)
