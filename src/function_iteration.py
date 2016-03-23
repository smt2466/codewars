"""Function iteration
http://www.codewars.com/kata/54b679eaac3d54e6ca0008c9

The purpose of this kata is to write a higher-order function which is capable
of creating a function that iterates on a specified function a given number of
times. This new functions takes in an argument as a seed to start the
computation from.

For instance, consider the function getDouble. When run twice on value 3,
yields 12 as shown below.

    getDouble(3) => 6
    getDouble(6) => 12

Let us name the new function createIterator and we should be able to obtain
the same result using createIterator as shown below:

    // This means, it runs *getDouble* twice
    var doubleIterator = createIterator(getDouble, 2);
    doubleIterator(3) => 12

For the sake of simplicity, all function inputs to createIterator would be
functions returning a small number and number of iterations would always be
integers.
"""


def create_iterator(func, num):
    """Create a function, that will apply func num times to it's argument

    Args:
        func: Function to apply
        num (int): Number of apply iteration

    Returns:
        function

    Examples:
        >>> triple_iterator = create_iterator(lambda x: 3*x, 2)
        >>> triple_iterator(3)
        27

    """
    def inner(arg):
        """Apply func num times to arg

        Args:
            arg (int)

        Returns:
            int
        """
        acc = arg
        for _ in range(num):
            acc = func(acc)
        return acc
    return inner
