# pylint: disable=invalid-name

"""Fuel Calculator
https://www.codewars.com/kata/fuel-calculator

In this kata you will have to write a function called `fuelPrice` (`fuel_price`
in PHP) that takes `litres` and `pricePerLiter` as arguments. Purchases of 2 or
more litres get a discount of 5 cents per litre, purchases of 4 or more litres
get a discount of 10 cents per litre, and so on every two litres, up to a
maximum discount of 25 cents per litre. But total discount per liter cannot be
more than 25 cents. round answer to 2 decimal places. Also you can guess that
there will not be negative or non-numeric inputs.

!Good Luck!
"""


def fuelPrice(litres, price):
    """Counts fuel price with discount based on litres value"""
    if litres < 2:
        discount = 0
    elif litres < 4:
        discount = .5*litres
    elif litres < 6:
        discount = .10*litres
    elif litres < 8:
        discount = .15*litres
    elif litres < 10:
        discount = .20*litres
    else:
        discount = .25*litres
    return round(litres*price - discount, 2)
