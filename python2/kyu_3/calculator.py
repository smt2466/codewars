# pylint: disable=eval-used, too-few-public-methods, missing-docstring

"""Calculator
https://www.codewars.com/kata/calculator

Create a simple calculator that given a string of operators (+ - * and /) and
numbers separated by spaces returns the value of that expression

Remember about the order of operations! Multiplications and divisions have a
higher priority and should be performed left-to-right. Additions and
subtractions have a lower priority and should also be performed left-to-right.
"""


class Calculator(object):

    @staticmethod
    def evaluate(code):
        return eval(code)
