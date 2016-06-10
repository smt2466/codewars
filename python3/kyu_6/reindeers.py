"""How Many Reindeers?
https://www.codewars.com/kata/52ad1db4b2651f744d000394

Santa puts all the presents into the huge sack. In order to let his reindeers
rest a bit, he only takes as many reindeers with him as he is required to do.
The others may take a nap.

Two reindeers are always required for the sleigh and Santa himself.
Additionally he needs 1 reindeer per 30 presents. As you know, Santa has
8 reindeers in total, so he can deliver up to 180 presents at once (2 reindeers
for Santa and the sleigh + 6 reindeers with 30 presents each).

Complete the function reindeers(), which takes a number of presents and returns
the minimum numbers of required reindeers. If the number of presents is too
high, throw an error.
"""

import math


def reindeer(presents):
    """Calculate number of reindeers for Santa

    Args:
        presents (int): Number of presents

    Returns:
        int: Number of reindeers

    Raises:
        ValueError if too many presents for eight reindeers

    Examples:
        >>> reindeer(60)
        4
        >>> reindeer(181)
        Traceback (most recent call last):
            ...
        ValueError: Too many presents!
    """
    additional_reindeers = math.ceil(presents/30)
    if additional_reindeers > 6:
        raise ValueError('Too many presents!')
    else:
        return 2 + additional_reindeers
