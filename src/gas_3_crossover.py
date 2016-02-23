# coding=utf-8

""""Genetic Algorithm Series - #3 Crossover
http://www.codewars.com/kata/567d71b93f8a50f461000019

In genetic algorithms, crossover is a genetic operator used to vary the
programming of chromosomes from one generation to the next.

In this kata you have to implement a function crossover that receives two
chromosomes chromosome1, chromosome2 and a zero-based index and it has to
return an array with the crossover result on both chromosomes [chromosome1,
chromosome2].
"""


def crossover(chromosome1, chromosome2, index):
    """Cross chromosomes

    Args:
        chromosome1 (str): Sequence of gens '101010'
        chromosome2 (str): Sequence of gens '101010'
        index (int): Crossover start position

    Returns:
        list: [chromosome1`, chromosome2`] after crossover

    Examples:
        >>> crossover('111', '000', 1)
        ['100', '011']
    """
    first = chromosome1[:index] + chromosome2[index:]
    second = chromosome2[:index] + chromosome1[index:]
    return [first, second]
