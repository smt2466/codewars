"""N-th Fibonacci
http://www.codewars.com/kata/522551eee9abb932420004a0

I love Fibonacci numbers in general, but I must admit I love some more than
others.

I would like for you to write me a function that when given a number (n)
returns the n-th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are 0 and 1,
and each subsequent number is the sum of the previous two.
"""


def nth_fib(num):
    """Return nth fibonacci number

    Args:
        num (int)

    Returns:
        int: nth fibonacci number

    Examples:
        >>> nth_fib(10)
        34
    """
    tmp = [0, 1]
    if num < 3:
        return tmp[num - 1]
    for _ in range(num - 2):
        tmp[0], tmp[1] = tmp[1], sum(tmp)
    return tmp[1]
