# 222, Simple DFS | O(N) and O(log(N))
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: Optional[TreeNode]) -> int:
    def dfs(node):
        if node is None:
            return 0
        count = 1 + dfs(node.left) + dfs(node.right)

        return count

    return dfs(root)
