"""Are they the "same"?
https://www.codewars.com/kata/are-they-the-same

Given two arrays `a` and `b` write a function `comp(a, b)` (`compSame(a, b)` in
Clojure) that checks whether the two arrays have the "same" elements, with the
same multiplicities. "Same" means, here, that the elements in `b` are the
elements in `a` squared, regardless of the order.

## Remarks

`a` or `b` might be `[]` (all languages).

`a` or `b` might be `nil` or `null` or `None` (except in Haskell, Elixir, C++).

If `a` or `b` are `nil` (or `null` or `None`), the problem doesn't make sense so
return false.

If `a` or `b` are empty the result is evident by itself.
"""


def comp(arr1, arr2):
    """Compares two arrays"""
    try:
        return sorted(item**2 for item in arr1) == sorted(arr2)
    except TypeError:
        return False
