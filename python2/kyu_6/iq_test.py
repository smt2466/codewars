# pylint: disable=expression-not-assigned

""""IQ Test
http://www.codewars.com/kata/552c028c030765286c00007d

Bob is preparing to pass IQ test. The most frequent task in this test is to
find out which one of the given numbers differs from the others. Bob observed
that one number usually differs from the others in evenness. Help Bob - to
check his answers, he needs a program that among the given numbers finds one
that is different in evenness, and return a position of this number.

Keep in mind that your task is to help Bob solve a real IQ test, which means
indexes of the elements start from 1 (not 0)
"""


def iq_test(nums):
    """One number is odd while other are even, or vise versa - find it

    Args:
        nums (str): '1 2 11 ...'

    Returns:
        int: Position of differ number + 1

    Examples:
        >>> iq_test('2 4 6 7 8')
        4
    """
    odd = []
    even = []
    for i, num in ((i, int(num)) for (i, num) in enumerate(nums.split(' '))):
        odd.append((i, num)) if num % 2 != 0 else even.append((i, num))
        if len(odd) > 1 and even:
            return even[0][0] + 1
        elif len(even) > 1 and odd:
            return odd[0][0] + 1
