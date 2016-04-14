# pylint: disable=invalid-name

"""Binary Tree Compare
http://www.codewars.com/kata/55847fcd3e7dadc9f800005f

Given the node object:

Node:
  val: <int>,
  left: <Node> or null,
  right: <Node> or null

write a function compare(a, b) which compares the two trees defined by Nodes
a and b and returns true if they are equal in structure and in value and false
otherwise.
"""


def compare(a, b):
    """Compare two binary trees

    Args:
        a: First node
        b: Second node

    Returns:
        bool: Equal or not
    """
    if a and b:
        return a.val == b.val \
               and compare(a.left, b.left) \
               and compare(a.right, b.right)
    else:
        return a == b
