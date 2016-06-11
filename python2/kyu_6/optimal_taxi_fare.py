"""Optimal Taxi Fare
https://www.codewars.com/kata/52f51502053125863c0009d7

The student needs to get on a train that leaves from the station D kilometres
away in T minutes.

She can get a taxi that drives at V1 km/h for the price of R euro/km or she can
walk at V2 km/h for free.

A correct solution will be a function that returns the minimum price she needs
to pay the taxi driver or the string "Won't make it!".

All the inputs will be positive integers, the output has to be a string
containing a number with two decimal places - or "Won't make it!" if that is
the case.

It won't take her any time to get on the taxi or the train.

In non-trivial cases you need to combine walking and riding the taxi so that
she makes it, but pays as little as possible.
"""


def calculate_optimal_fare(distance, time, taxi_speed, rate, walk_speed):
    """Calculate minimum price

    Args:
        distance (int): Distance to station in kms
        time (int): Maximum time in minutes
        taxi_speed (int): km/h
        rate (int): Taxi rate in euro/km
        walk_speed (int): km/h

    Returns:
        str: Minimum price or "Won't make it!"
    """
    # Can simply walk?
    if distance*1./walk_speed <= time/60.:
        return '0.00'

    # Optimal distance by taxi
    taxi = (time/60. - distance*1./walk_speed)/(1./taxi_speed - 1./walk_speed)

    # Not enough time
    if taxi > distance or taxi < 0:
        return "Won't make it!"

    return '{0:.2f}'.format(rate*taxi)
