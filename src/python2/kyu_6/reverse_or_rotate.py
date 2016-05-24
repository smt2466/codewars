"""Reverse or rotate?
http://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991

The input is a string str of digits. Cut the string into chunks of size sz
(ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is
divisible by 2, reverse it; otherwise rotate it to the left by one position.
Put together these modified chunks and return the result as a string.

If

    sz is <= 0 or if str is empty return ""
    sz is greater (>) than the length of str it is impossible to take a chunk
        of size sz hence return "".
"""


def revrot(string, size):
    """Cut string to chunks of equal size and revert chunk if it's sum of
    cubes of digits divisible by 2 else rotate left by 1

    Args:
        string (str): Original string
        size (int): Size of chunks

    Returns:
        str: Modified string

    Examples:
        >>> revrot('123456987654', 6)
        '234561876549'
    """
    if not size:
        return ''

    chunks = [string[i:i+size] for i in range(0, len(string), size)]
    if len(chunks[-1]) != size:
        chunks.pop()

    result = []
    for chunk in chunks:
        if sum(int(digit)**3 for digit in chunk) % 2 == 0:
            result.append(chunk[::-1])
        else:
            result.append(chunk[1:] + chunk[0])

    return ''.join(result)
