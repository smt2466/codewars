# pylint: disable=invalid-name

""""Sum of many ints
http://www.codewars.com/kata/54c2fc0552791928c9000517

For i from 1 to n, do i % m and return the sum

    f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)

You'll need to get a little clever with performance, since n can be a very
large number
"""


def f(limit, divisor):
    """Compute sum of int % divisor from 1 to limit

    Args:
        limit (int or float): Range top border
        divisor (int or float)

    Returns:
        int or float: Sum of divisions

    Examples:
        >>> f(13, 10)
        51
    """
    chain = divisor*(divisor - 1)/2
    full_chains = chain*(limit//divisor)
    part_chain = (1 + limit % divisor)*(limit % divisor)/2
    return full_chains + part_chain
