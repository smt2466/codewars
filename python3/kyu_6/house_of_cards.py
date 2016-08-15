"""House of cards
https://www.codewars.com/kata/house-of-cards

You want to build a standard house of cards, but you don't know how many cards
you will need. Write a program which will count the minimal number of cards
according to the number of floors you want to have. For example, if you want
a one floor house, you will need 7 of them (two pairs of two cards on the base
floor, one horizontal card and one pair to get the first floor). Here you can
see which kind of house of cards I mean:
http://www.wikihow.com/Build-a-Tower-of-Cards

### Details (Ruby & JavaScript & Python)
The input must be an integer greater than 0, for other input raise an error.

### Details (Haskell)
The input must be an integer greater than 0, for other input return `Nothing`.
"""


def house_of_cards(floors):
    """Calculates number of card for card house"""
    if floors < 1:
        raise ValueError
    else:
        return (floors + 1)*(1.5*floors + 2)
