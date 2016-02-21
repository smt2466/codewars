# coding=utf-8

""""Fix the Bugs (Syntax)
http://www.codewars.com/kata/56aed32a154d33a1f3000018/train/python

In this Kata you should try to fix all the syntax errors found in the code.

Once you think all the bugs are fixed run the code to see if it works.
A correct solution should return:

    - false if either of the arguments are not numbers
    - a % b plus b % a if both arguments are numbers
"""


def my_first_kata(first, second):
    """a % b plus b % a if both arguments are numbers else False

    Args:
        first (int)
        second (int)

    Returns:
        int or False
    """
    try:
        if not (isinstance(first, bool) or isinstance(second, bool)):
            return first % second + second % first
        else:
            return False
    except (TypeError, ZeroDivisionError):
        return False
