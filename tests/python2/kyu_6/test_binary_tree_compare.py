# pylint: disable=missing-docstring, invalid-name, too-few-public-methods

"""Binary Tree Compare"""

import pytest

from python2.kyu_6.binary_tree_compare import compare


class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

a_node = Node(1, None, None)
b_node = Node(1, None, None)
c_node = Node(2, None, None)

EXAMPLES = (
    ('first_node', 'second_node', 'expected'),
    [
        (a_node, b_node, True),
        (a_node, c_node, False)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(first_node, second_node, expected):
    assert compare(first_node, second_node) == expected
