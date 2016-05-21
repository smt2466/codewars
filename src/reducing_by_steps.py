# pylint: disable=invalid-name

"""Reducing by steps
http://www.codewars.com/kata/56efab15740d301ab40002ee

Data: an array of integers, a function f of two variables and an init value.

Example: a = [2, 4, 6, 8, 10, 20], f(x, y) = x + y; init = 0

Output: an array of integers, say r, such that

r = [r[0] = f(init, a[0]), r[1] = f(r[0], a[1]), r[2] = f(r[1], a[2]), ...]

With our example: r = [2, 6, 12, 20, 30, 50]

Task:

Write the following functions of two variables

    - som : (x, y) -> x + y
    - mini : (x, y) -> min(x, y)
    - maxi : (x, y) -> max(x, y)
    - lcmu : (x, y) -> lcm(abs(x), abs(y) (see note for lcm)
    - gcdi : (x, y) -> gcd(abs(x), abs(y) (see note for gcd)

and

    - function oper_array(fct, arr, init) (or operArray or oper-array) where
        - fct is the function of to variables to apply to the array arr
          (fct will be one of som, mini, maxi, lcmu or gcdi)
        - init is the initial value

Notes:

    - The form of the parameter fct in oper_array (or operArray or oper-array)
      changes according to the language. You can see each form according to the
      language in "Your test cases".
    - AFAIK there are no corner cases, everything is as nice as possible.
    - lcm and gcd see: https://en.wikipedia.org/wiki/Least_common_multiple
      https://en.wikipedia.org/wiki/Greatest_common_divisor
    - you could google "reduce function (your language)" to have a general view
      about the reduce functions.
"""

from fractions import gcd


def gcdi(a, b):
    """gcd(abs(x), abs(y)"""
    return gcd(abs(a), abs(b))


def lcmu(a, b):
    """(x, y) -> lcm(abs(x), abs(y)"""
    return (abs(a)*abs(b))//gcdi(a, b)


def som(a, b):
    """(x, y) -> x + y"""
    return a + b


def maxi(a, b):
    """(x, y) -> max(x, y)"""
    return max(a, b)


def mini(a, b):
    """(x, y) -> min(x, y)"""
    return min(a, b)


def oper_array(fct, arr, init):
    """Apply fct to arr items by pairs

    Args:
        fct (function): Function to apply
        arr (list): Array of integers
        init (integer): Initial reduce value

    Returns:
        list: Array after pairwise function applying

    Examples:
        >>> oper_array(som, [1, 2, 3, 4, 5], 0)
        [1, 3, 6, 10, 15]
    """
    result = []
    for i, item in enumerate(arr):
        result.append(fct(result[i-1] if result else init, item))
    return result
