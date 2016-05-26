"""Checking Groups
http://www.codewars.com/kata/54b80308488cb6cd31000161

In English and programming, groups can be made using symbols such as "()"
and "{}" that change meaning. However, these groups must be closed in the
correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for
correct grouping.

A correct string cannot close groups in the wrong order, open a group but
fail to close it, or close a group before it is opened.

Your function will take an input string that may contain any of the symbols
"()" "{}" or "[]" to create groups.

It should return True if the string is empty or otherwise grouped correctly,
or False if it is grouped incorrectly.
"""

BRACES = {'(': ')', '[': ']', '{': '}'}


def group_check(groups):
    """Check if all braces correctly closed

    Args:
        groups (str): String of {}[]()

    Returns:
        bool: True if all braces correctly close else False

    Examples:
        >>> group_check('([]{}[])')
        True
        >>> group_check('([)]')
        False
    """
    to_be_closed = []
    for char in groups:
        if char in BRACES.keys():
            to_be_closed.append(BRACES[char])
        else:
            try:
                closed = to_be_closed.pop()
            except IndexError:
                return False
            if char != closed:
                return False
    return not to_be_closed
