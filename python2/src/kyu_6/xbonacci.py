# pylint: disable=invalid-name

"""Fibonacci, Tribonacci and friends
http://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python

If you have completed the Tribonacci sequence kata, you would know by now that
mister Fibonacci has at least a bigger brother. If not, give it a quick look
to get how things work.

Well, time to expand the family a little more: think of a Quadribonacci
starting with a signature of 4 elements and each following element is the sum
of the 4 previous, a Pentabonacci (well Cinquebonacci would probably sound
a bit more italian, but it would also sound really awful) with a signature
of 5 elements and each following element is the sum of the 5 previous, and
so on.

Well, guess what? You have to build a Xbonacci function that takes
a signature of X elements - and remember each next element is the sum
of the last X elements - and returns the first n elements of the so seeded
sequence.
"""


def Xbonacci(signature, number):
    """Return Xbonacci sequence

    Args:
        signature (list): First n elements (int)
        number (int): Number of elements in sequence

    Returns:
        list: Xbonacci sequence

    Examples:
        >>> Xbonacci([0, 1, 2, 3], 6)
        [0, 1, 2, 3, 6, 12]
    """
    if number < len(signature):
        return signature[:number]
    else:
        sequence = list(signature)
        while number - len(signature) > 0:
            sequence.append(sum(sequence[-len(signature):]))
            number -= 1
        return sequence
