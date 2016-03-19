""""longest_palindrome
http://www.codewars.com/kata/54bb6f887e5a80180900046b

Longest Palindrome

Find the length of the longest substring in the given string s that is the
same in reverse.

As an example, if the input was 'I like racecars that go fast', the substring
(racecar) length would be 7.

If the length of the input string is 0, return value must be 0.
"""


def longest_palindrome(text):
    """Find the length of the longest palindrome

    Args:
        text (str): String to find palindromes

    Returns:
        int: Max length of palindrome in text

    Examples:
        >>> longest_palindrome('a')
        1
        >>> longest_palindrome('aab')
        2
        >>> longest_palindrome('abcde')
        1
        >>> longest_palindrome('zzbaabcd')
        4
        >>> longest_palindrome('')
        0
    """
    for length in range(len(text), 0, -1):
        for pos in range(0, len(text) - length + 1):
            substring = text[pos:pos + length]
            if substring == substring[::-1]:
                return length
    return 0
