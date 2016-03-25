"""Sum consecutives
http://www.codewars.com/kata/55eeddff3f64c954c2000059

You are given a list/array which contains only integers (positive and
negative). Your job is to sum only the numbers that are the same and
consecutive. The result should be one list.

Extra credit if you solve it in one line. You can asume there is never an
empty list/array and there will always be an integer.

Same meaning: 1 == 1

1 != -1
"""


def sum_consecutives(sequence):
    """Sum consecutive numbers in array

    Args:
        sequence (list): List of integers

    Returns:
        list: List of integers without consecutively equal

    Examples:
        >>> sum_consecutives([1, 1, 1, 2, 2])
        [3, 4]
    """
    current = None
    current_sum = 0
    result = []

    for item in sequence:
        if current == item:
            current_sum += current
        else:
            if current is not None:
                result.append(current_sum)
            current_sum = current = item

    result.append(current_sum)
    return result
