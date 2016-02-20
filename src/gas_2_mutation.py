# coding=utf-8

"""Genetic Algorithm Series - #2 Mutation
http://www.codewars.com/kata/567b39b27d0a4606a5000057

Mutation is a genetic operator used to maintain genetic diversity from one
generation of a population of genetic algorithm chromosomes to the next.

A mutation here may happen on zero or more positions in a chromosome.
It is going to check every position and by a given probability it will decide
if a mutation will occur.

A mutation is the change from 0 to 1 or from 1 to 0.

Note: Some tests are random. If you think your algorithm is correct but the
result fails, trying again should work.
"""

from random import random


def mutate_gen(gen, prob):
    """Mutate one gen

    Args:
        gen (str): '0' or '1'
        prob (float): Mutation probability 0..1

    Returns:
        str: '1' or '0'

    Examples:
        >>> mutate_gen('1', 1)
        '0'
        >>> mutate_gen('0', 1)
        '1'
        >>> mutate_gen('1', 0)
        '1'
    """
    return str(int(not int(gen))) if random() < prob else gen


def mutate(chromosome, prob):
    """Mutate sequence of gens

    Args:
        chromosome (str): Sequence of gens '110010110'
        prob (float): Gen mutation probability

    Returns:
        str: Mutation result '001101001'

    Examples:
        >>> mutate('101010', 1)
        '010101'
        >>> mutate('101010', 0)
        '101010'
    """
    return ''.join(mutate_gen(gen, prob) for gen in chromosome)
