# 100, DFS |O(N) and O(2^N) where N is the height of the tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    qo = []
    po = []

    def dfs(node, array):
        if node is None:
            array.append(None)
            return

        array.append(node.val)
        dfs(node.left, array)
        dfs(node.right, array)

    dfs(p, po)
    dfs(q, qo)

    if len(po) != len(qo):
        return False

    for idx in range(len(po)):
        if po[idx] != qo[idx]:
            return False
    return True
