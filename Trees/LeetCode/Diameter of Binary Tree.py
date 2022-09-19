# 543, Using Tree height calculation and DFS | O(N) and O(2^N)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    max_len = [0]

    def dfs(node):
        if node is None:
            return 0

        left = dfs(node.left)

        if left == -1:
            return -1

        right = dfs(node.right)

        if right == -1:
            return - 1

        max_len[0] = max(max_len[0], left + right)

        return 1 + max(left, right)

    dfs(root)

    return max_len[0]

