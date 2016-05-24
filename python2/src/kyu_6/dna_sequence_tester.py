# pylint: disable=invalid-name

"""DNA Sequence Tester
http://www.codewars.com/kata/56fbb2b8fca8b97e4d000a31

DNA is a biomolecule that carries genetic information. It is composed of four
different building blocks, called nucleotides: adenine (A), thymine (T),
cytosine (C) and guanine (G). Two DNA strands join to form a double helix,
whereby the nucleotides of one strand bond to the nucleotides of the other
strand at the corresponding positions. The bonding is only possible if the
nucleotides are complementary: A always pairs with T, and C always pairs
with G.

Due to the asymmetry of the DNA, every DNA strand has a direction associated
with it. The two strands of the double helix run in opposite directions to
each other, which we refer to as the 'up-down' and the 'down-up' directions.

Write a function checkDNA that takes in two DNA sequences as strings, and
checks if they are fit to form a fully complementary DNA double helix. The
function should return a Boolean true if they are complementary, and false if
there is a sequence mismatch (Example 1 below).

Note:

    - All sequences will be of non-zero length, and consisting only of A, T, C
      and Gcharacters.
    - All sequences will be given in the up-down direction.
    - The two sequences to be compared can be of different length. If this is
      the case and one strand is entirely bonded by the other, and there is no
      sequence mismatch between the two (Example 2 below), your function should
      still return true.
    - If both strands are only partially bonded (Example 3 below), the function
      should return false.
"""


def pair(*args):
    """Compare two nucleotide

    Args:
        args: Two nucleotide

    Returns:
        bool: True if nucleotides are complementary else False

    Examples:
        >>> pair('A', 'T')
        True
        >>> pair('A', 'C')
        False
    """
    return set(args) in ({'A', 'T'}, {'C', 'G'})


def check_DNA(seq1, seq2):
    """Check if two DNA sequence are bonding

    Args:
        seq1 (str): DNA sequence [ATGC]+
        seq2 (str): DNA sequence [ATGC]+

    Returns:
        bool: True if bonding else False

    Examples:
        >>> check_DNA('ATGC', 'GCAT')
        True
        >>> check_DNA('ATGCATGC', 'GCAT')
        True
        >>> check_DNA('ATGC', 'AAAA')
        False
    """
    shortest = (seq1 if len(seq2) > len(seq1) else seq2)[::-1]
    longest = seq2 if len(seq2) > len(seq1) else seq1

    for i, _ in enumerate(longest):
        for j, char2 in enumerate(shortest):
            if not pair(longest[i + j], char2) and \
                    len(shortest) + i > len(longest):
                return False
            elif not pair(longest[i + j], char2):
                break
        else:
            return True
