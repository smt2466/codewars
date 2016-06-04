"""Collatz
http://www.codewars.com/kata/5286b2e162056fd0cb000c20

A collatz sequence, starting with a positive integern, is found by repeatedly
applying the following function to n until n == 1 :

    n = { n / 2 for even n ;
          3n + 1 for odd n }

A more detailed description of the collatz conjecture may be found on Wikipedia.

Create a function collatz that returns a collatz sequence string starting with
the positive integer argument passed into the function, in the following form:

    "X0->X1->...->XN"

Where Xi is each iteration of the sequence and N is the length of the sequence.

    collatz(4) # should return "4->2->1"
    collatz(3) # should return "3->10->5->16->8->4->2->1"

Don't worry about invalid input. Arguments passed into the function are
guaranteed to be valid integers >= 1.
"""


def icollatz(num):
    """Collatz sequence generator

    Args:
        num (int): Sequence first number

    Yields:
        str: Next sequence number converted to str

    Examples:
        >>> gen = icollatz(3)
        >>> next(gen)
        '3'
        >>> next(gen)
        '10'
        >>> next(gen)
        '5'
    """
    yield str(num)
    while num != 1:
        num = num/2 if num % 2 == 0 else 3*num + 1
        yield str(num)


def collatz(num):
    """Create collatz sequence start with num

    Args:
        num (int): First sequence number

    Returns:
        str: Sequence as a string with '->' as number separator

    Examples:
        >>> collatz(5)
        '5->16->8->4->2->1'
    """
    return '->'.join(icollatz(num))
