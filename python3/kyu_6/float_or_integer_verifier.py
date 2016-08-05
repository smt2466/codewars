"""Float or Integer verifier
https://www.codewars.com/kata/float-or-integer-verifier

Write a function that verifies provided argument is either an integer or a
floating-point number, returning true if it is or false otherwise.


*__Pointers__*

* Numeric quantities are _signed_ (optionally when positive, e.g. "+5" is
  valid notation)
* Floats less than 1 (___not considering possible exponent!___) can be
  written without a leading "0" (e.g. ".00001")
* Order-of-magnitude (i.e. 10, 100, 1000, etc.) can be written in
  [E notation](http://en.wikipedia.org/wiki/Scientific_notation)
  (the exponent is also signed, optionally so if positive, e.g. all the
  following are valid 1e2, 1E2, 1e-2, 1E-2, 1e+2)
* Probably obvious, but no spaces are allowed anywhere (we aim to represent
  a real-life number)
* You can mix-n'-match any or all above pointers in any single numeric quantity
"""


def i_or_f(number):
    """Is number a float or integer?"""
    try:
        float(number)
    except ValueError:
        return False
    else:
        return True
