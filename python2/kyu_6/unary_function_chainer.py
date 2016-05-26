"""Unary function chainer
http://www.codewars.com/kata/54ca3e777120b56cb6000710

Your task is to write a higher order function for chaining together a list
of unary functions. In other words, it should return a function that does
a left fold on the given functions.

    chained([a,b,c,d])(input)

Should yield the same result as

    d(c(b(a(input))))
"""


def chained(functions):
    """Create a function that will apply all functions to it's argument

    Args:
        functions (list): List of functions to apply

    Returns:
        function
    """
    def inner(arg):
        """Apply functions to arg

        Args:
            arg: Any argument to apply functions to
        """
        for func in functions:
            arg = func(arg)
        return arg
    return inner
