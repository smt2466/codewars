"""Hamming Distance
https://www.codewars.com/kata/hamming-distance

The [Hamming Distance](http://en.wikipedia.org/wiki/Hamming_distance)
is a measure of similarity between two strings of equal length. Complete the
function so that it returns the number of positions where the input strings do
not match.

Examples (in JavaScript):

```
hamming("I like turtles","I like turkeys")  //returns 3
hamming("Hello World","Hello World")  //returns 0
```

You can assume that the two input strings are of equal length.
"""


def hamming(txt1, txt2):
    """Computes hamming distance of two strings"""
    return sum(bool(ord(chr1) - ord(chr2)) for chr1, chr2 in zip(txt1, txt2))
