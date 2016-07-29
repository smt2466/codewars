"""Feynman's square question
https://www.codewars.com/kata/feynmans-square-question

# Feynman's squares
Richard Phillips Feynman was a well-known American physicist and a recipient of
the Nobel Prize in Physics. He worked in theoretical physics and pioneered the
field of quantum computing.

Recently, an old farmer found some papers and notes that are believed to have
belonged to Feynman. Among notes about mesons and electromagnetism, there was
a napkin where he wrote a simple puzzle: "how many different squares are there
in a grid of NxN squares?".

For example, when N=2, the answer is 5: the 2x2 square itself, plus the four
1x1 squares in its corners:

# Task

You have to write a function count_squares that solves Feynman's question in
general. The input to your function will always be a positive integer.
"""


def count_squares(num):
    """Counts number of sub-squares in num x num square"""
    return sum((num - i)**2 for i in range(num))
