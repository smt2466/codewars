# pylint: disable=invalid-name

"""Modular Multiplicative Inverse
https://www.codewars.com/kata/modular-multiplicative-inverse

A common problem in number theory is to find x given a such that:

a * x = 1 mod [n]

Then x is called the inverse of a modulo n.

Your goal is to code a function inverseMod which take a and n as parameters and
return x.

You may be interested by these pages:

http://en.wikipedia.org/wiki/Modular_multiplicative_inverse

http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

a and n should be co-prime to have a solution, if it is not the case, you
should return None (Python), nil (Ruby) or null (Javascript).

a and n will be positive integers. The problem can easily be generalised to
negative integer with some sign changes so we won't deal with them.
"""


def gcd_ext(a, b):
    """Extended GCD"""
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = gcd_ext(b, a % b)
        return y, x - y * (a // b), gcd


def inverseMod(a, n):
    """Computes modular multiplicative inverse"""
    x, _, gcd = gcd_ext(a, n)
    if gcd == 1:
        return x % n
    else:
        return None
