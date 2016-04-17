"""Vasya - Clerk
http://www.codewars.com/kata/555615a77ebc7c2c8a0000b8

The new "Avengers" movie has just been released! There are a lot of people
at the cinema box office standing in a huge line. Each of them has a single
100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every
single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially
has no money and sells the tickets strictly in the order people follow in the
line?

Return YES, if Vasya can sell a ticket to each person and give the change.
Otherwise return NO.
"""


def tickets(people):
    """Check if clerk can sell all tickets and give the charge

    Args:
        people (list): List of bills, where bill belongs to [25, 50, 100]

    Returns:
        str: 'YES' or 'NO'

    Examples:
        >>> tickets([25, 25, 100])
        'NO'
        >>> tickets([25, 25, 50, 100])
        'YES'
    """
    bill_25, bill_50 = 0, 0

    for bill in people:
        if bill == 25:
            bill_25 += 1
        elif bill == 50 and bill_25:
            bill_25 -= 1
            bill_50 += 1
        elif bill == 100 and bill_50 and bill_25:
            bill_25 -= 1
            bill_50 -= 1
        elif bill == 100 and bill_25 > 2:
            bill_25 -= 3
        else:
            return 'NO'
    return 'YES'
