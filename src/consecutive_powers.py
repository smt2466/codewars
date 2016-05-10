"""Take a Number And Sum Its Digits Raised To The Consecutive Powers
http://www.codewars.com/kata/5626b561280a42ecc50000d1

The number 89 is the first integer with more than one digit that fulfills
the property partially introduced in the title of this kata. What's the use
of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers
a, b that defines the range [a, b] (inclusive) and outputs a list of the
sorted numbers in the range that fulfills the property described above.

Let's see some cases:

    sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

If there are no numbers of this kind in the range [a, b] the function should
output an empty list.

    sum_dig_pow(90, 100) == []
"""


def check_powers(number):
    """Check if consecutive powers sum of number is equal to number itself

    Args:
        number (int): Number to check

    Returns:
        bool

    Examples:
        >>> check_powers(1)
        True
        >>> check_powers(12)
        False
    """
    new = sum(int(char)**(i + 1) for i, char in enumerate(str(number)))
    return number == new


def sum_dig_pow(start, stop):
    """Return list of all number with consecutive powers sum property
    from the given range

    Args:
        start (int): Range start
        stop (int): Range stop (including)

    Returns:
        list: List of appropriate numbers

    Examples:
        >>> sum_dig_pow(5, 12)
        [5, 6, 7, 8, 9]
        >>> sum_dig_pow(13, 20)
        []
    """
    return [num for num in range(start, stop + 1) if check_powers(num)]
