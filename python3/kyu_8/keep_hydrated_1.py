"""Keep Hydrated!
https://www.codewars.com/kata/keep-hydrated-1

Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of
water per hour of cycling.

You get given the time and you need to return the number of litres Nathan will
drink, rounded to the smallest value.

For example:

    time = 3 ----> litres = 1
    time = 6.7---> litres = 3
    time = 11.8--> litres = 5
"""


def litres(time):
    """Calculates number of liters of water to drink after given hours of
    training

    Args:
        time (float, int): Number of hours

    Returns:
        int: Number of litres

    Examples:
        >>> litres(4)
        2
        >>> litres(5)
        2
    """
    return int(time*0.5)
