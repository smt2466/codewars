# pylint: disable=missing-docstring

"""DNA Sequence Tester"""

import pytest

from src.dna_sequence_tester import check_DNA, pair

DNA = (
    ('seq1', 'seq2', 'expected'),
    [
        ('GTCTTAGTGTAGCTATGCATGC', 'GCATGCATAGCTACACTACGAC', False),
        ('ATGCTACG', 'CGTAGCAT', True),
        ('AGTCTGTATGCATCGTACCC', 'GGGTACGATGCATACAGACT', True),
        ('TGCTACGTACGATCGACGATCCACGAC', 'GTCGTGGATCGTCGATCGTACGTAGCA', True),
        ('ATGCCTACGGCCATATATATTTAG', 'CTAAATATGTATGGCCGTAGGCAT', False),
        ('GTCACCGA', 'TCGGCTGAC', False),
        ('TAATACCCGACTAATTCCCC', 'GGGGAATTTCGGGTATTA', False),
        ('GCTAACTCGAAGCTATACGTTA', 'TAACGTATAGCTTCGAGGTTAGC', False),
        ('GCGCTGCTAGCTGATCGA', 'ACGTACGATCGATCAGCTAGCAGCGCTAC', True),
        ('GCTAGCACCCATTAGGAGATAC', 'CTCCTAATGGGTG', True),
        ('TAGCATCGCCAAATTATGCGTCAGTCTGCCCG', 'GGGCA', True),
        ('ACGACTACGTGCGCCGCTAATATT', 'GCACGGGTCGT', False),
        ('CGATACGAACCCATAATCG', 'CTACACCGGCCGATTATGG', False),
        ('CGACATCGAGGGGGCTCAGAAGTACTGA', 'CATGGCGTCAGTACTTCTGAGCC', False),
        ('GAGCAGTTGGTAGTTT', 'GTATCGAAACTACCA', False),
        ('TACGATCCAAGGCTACTCAGAG', 'GGGATACTCTGAGTAGCCTTGGAA', False),
    ]
)


NUCLEOTIDES = (
    ('nucleotide1', 'nucleotide2', 'expected'),
    [
        ('A', 'T', True),
        ('T', 'A', True),
        ('C', 'G', True),
        ('G', 'C', True),
        ('A', 'G', False),
        ('T', 'C', False),
    ]
)


@pytest.mark.parametrize(*DNA)
def test_returns_correct_result(seq1, seq2, expected):
    assert check_DNA(seq1, seq2) == expected


@pytest.mark.parametrize(*NUCLEOTIDES)
def test_nucleotide_pairs(nucleotide1, nucleotide2, expected):
    assert pair(nucleotide1, nucleotide2) == expected
