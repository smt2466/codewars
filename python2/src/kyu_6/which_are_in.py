"""Which are in?
http://www.codewars.com/kata/550554fd08b86f84fe000a58

Given two arrays of strings a1 and a2 return a sorted array r in
lexicographical order and without duplicates of the strings of a1 which are
sub strings of strings of a2.
"""


def in_array(array1, array2):
    """Find all words from array1 which are in words of array2

    Args:
        array1 (list): List of strings
        array2 (list): List of strings

    Returns:
        list: List of strings without duplicates

    Examples:
        >>> in_array(['a', 'a', 'b'], ['ac', 'de'])
        ['a']
    """
    result = []
    for word1 in array1:
        for word2 in array2:
            if word1 in word2:
                result.append(word1)
                break
    return sorted(set(result))
