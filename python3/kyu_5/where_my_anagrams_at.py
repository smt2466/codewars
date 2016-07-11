"""Where my anagrams at?
https://www.codewars.com/kata/where-my-anagrams-at

What is an anagram? Well, two words are anagrams of each other if they both
contain the same letters.

Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words. You should
return an array of all the anagrams or an empty array if there are none.
"""

from collections import Counter


def anagrams(goal, words):
    return [word for word in words if Counter(word) == Counter(goal)]
