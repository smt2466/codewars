"""Moves in squared strings (I)
http://www.codewars.com/kata/56dbe0e313c2f63be4000b25

This kata is the first of a sequence of four about "Squared Strings".

You are given a string of n lines, each substring being n characters long.
For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study some transformations of this square of strings.

    - Vertical mirror: vert_mirror (or vertMirror or vert-mirror)
      vert_mirror(s) => "dcba\nhgfe\nlkji\nponm"
    - Horizontal mirror: hor_mirror (or horMirror or hor-mirror)
      hor_mirror(s) => "mnop\nijkl\nefgh\nabcd"

or printed:

    vertical mirror   |horizontal mirror
    abcd --> dcba     |abcd --> mnop
    efgh     hgfe     |efgh     ijkl
    ijkl     lkji     |ijkl     efgh
    mnop     ponm     |mnop     abcd

Task:

    - Write these two functions

and

    - high-order function oper(fct, s) where
        + fct is the function of one variable f to apply to the string s
          (fct will be one of vertMirror, horMirror)

Examples:

    s = "abcd\nefgh\nijkl\nmnop"
    oper(vert_mirror, s) => "dcba\nhgfe\nlkji\nponm"
    oper(hor_mirror, s) => "mnop\nijkl\nefgh\nabcd"

Note:

The form of the parameter fct in oper changes according to the language.
You can see each form according to the language in "Your test cases".
Forthcoming katas will study other tranformations.
"""


def vert_mirror(strng):
    """Implement vertical mirror

    Args:
        strng (str): N lines of N length separated by '\n'

    Returns:
        str

    Examples:
        >>> s = 'abcd\\nefgh\\nijkl\\nmnop'
        >>> oper(vert_mirror, s)
        'dcba\\nhgfe\\nlkji\\nponm'
    """
    lines = strng.split('\n')
    return '\n'.join(line[::-1] for line in lines)


def hor_mirror(strng):
    """Implement horizontal mirror

    Args:
        strng (str): N lines of N length separated by '\n'

    Returns:
        str

    Examples:
        >>> s = 'abcd\\nefgh\\nijkl\\nmnop'
        >>> oper(hor_mirror, s)
        'mnop\\nijkl\\nefgh\\nabcd'
    """
    lines = strng.split('\n')
    return '\n'.join(lines[::-1])


def oper(fct, strng):
    """Apply fct to strng

    Args:
        fct (function): Function to apply
        strng (str): N lines of N length separated by '\n'

    Returns:
        str
    """
    return fct(strng)
