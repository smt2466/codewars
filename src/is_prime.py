"""Is a number prime?
http://www.codewars.com/kata/5262119038c0985a5b00029f

Define a function isPrime that takes one integer argument and returns true or
false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1
that has no positive divisors other than 1 and itself.

Assumptions

    You can assume you will be given an integer input.
    You can not assume that the integer will be only positive. You may be
    given negative numbers.
"""


def is_prime(num):
    """Check if number is a prime

    Args:
        num (int)

    Returns:
        bool

    Examples:
        >>> is_prime(5)
        True
    """
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, num/2, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True
