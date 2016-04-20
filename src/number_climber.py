"""Number Climber
http://www.codewars.com/kata/559760bae64c31556c00006b

For every positive integer N, there exists a unique sequence starting with 1
and ending with N and such that every number in the sequence is either the
double of the preceeding number or the double plus 1.

For example, given N = 13, the sequence is [1, 3, 6, 13], because . . . :

 3 =  2*1 +1
 6 =  2*3
 13 = 2*6 +1

Write a function that returns this sequence given a number N. Try generating
the elements of the resulting list in ascending order, i.e., without resorting
to a list reversal or prepending the elements to a list.
"""


def climb(num):
    """Find sequence which ends with num
    Each new item can be parent*2 or parent*2 + 1

    Args:
        num (int): End of sequence

    Returns:
        list: Sequence of integers ended with num

    Examples:
        >>> climb(13)
        [1, 3, 6, 13]
    """
    sequence = [num]
    while num != 1:
        num //= 2
        sequence.append(num)
    return sequence[::-1]
