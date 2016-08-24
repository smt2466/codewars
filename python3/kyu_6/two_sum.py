"""Two Sum
https://www.codewars.com/kata/two-sum

Write a function that takes an array of numbers (integers for the tests) and a
target number. It should find two different items in the array that, when added
together, give the target value. The indices of these items should then be
returned in an array like so: `[index1, index2]`.

For the purposes of this kata, some tests may have multiple answers; any valid
solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater,
and all of the items will be numbers; target will always be the sum of two
different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/
"""


def two_sum(numbers, target):
    """Find two item indexes which sum is equal to target"""
    for i, item1 in enumerate(numbers):
        for j, item2 in enumerate(numbers):
            if i != j and item1 + item2 == target:
                return [i, j]
