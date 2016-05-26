# coding=utf-8

"""80's Kids #4: Legends of the Hidden Temple
http://www.codewars.com/kata/56648a2e2c464b8c030000bf

You've made it through the moat and up the steps of knowledge. You've won the
temples games and now you're hunting for treasure in the final temple run.
There's good news and bad news. You've found the treasure but you've
triggered a nasty trap. You'll surely perish in the temple chamber.

With your last movements, you've decided to draw an "X" marks the spot for the
next archeologist.

Given an odd number, n, draw an X for the next crew. Follow the example below.

If n = 1 return 'X\n' and if you're given an even number or invalid input,
return '?'.

The output should be a string with no spaces after the final X on each line,
but a \n to indicate a new line.
"""


def mark_spot(num):
    """Draw the X

    Args:
        num (int): Left shift of the X center

    Returns:
        str
    """
    if isinstance(num, int) and num % 2 != 0 and num > 0:
        top = [' ' * i * 2 + 'X' + ' ' * (num * 2 - 3 - 4 * i) + 'X'
               for i in range(num / 2)]
        middle = [' ' * (num - 1) + 'X']
        bottom = top[::-1]
        return '\n'.join(top + middle + bottom) + '\n'
    else:
        return '?'
