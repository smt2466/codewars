"""Strip Comments
https://www.codewars.com/kata/strip-comments

Complete the solution so that it strips all text that follows any of a set of
comment markers passed in. Any whitespace at the end of the line should also be
stripped out.

**Example:**

Given an input string of:
```
apples, pears # and bananas
grapes
bananas !apples
```

The output expected would be:
```
apples, pears
grapes
bananas
```
"""

import re


def solution(text, markers):
    """Removes comments from text

    Args:
        text (str): Text strings with comments
        markers (list): List of comment markers

    Returns:
        >>> solution('hello world # comment', ['#'])
        'hello world'
    """
    markers = r'|'.join(re.escape(marker) for marker in markers)
    words = [re.split(markers, word)[0].rstrip() for word in text.split('\n')]
    return '\n'.join(words)
