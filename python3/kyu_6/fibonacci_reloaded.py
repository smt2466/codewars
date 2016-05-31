"""Fibonacci Reloaded
http://www.codewars.com/kata/52549d3e19453df56f0000fe

And here is Fibonacci again. This time we want to go one step further.
Our fib() function must be faster! Can you do it?

In case you don't know, what the Fibonacci number is:

The nth Fibonacci number is defined by the sum of the two previous Fibonacci
numbers. In our case: fib(1) == 0 and fib(2) == 1. With these initial values
you should be able to calculate each following Fibonacci number.
"""


def fib(num):
    """Find nth fibonacci number

    Args:
        num (int)

    Returns:
        int: nth fibonacci number

    Examples:
        >>> fib(8)
        13
    """
    tmp = [0, 1]
    for _ in range(num - 1):
        tmp[0], tmp[1] = tmp[1], sum(tmp)
    return tmp[0]
