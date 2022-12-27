# 1339, DFS to find Subtree Sum | O(N) and O(N)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxProduct(self, root: Optional[TreeNode]) -> int:
    self.values = []

    def dfs(node):
        if node:
            value = node.val + dfs(node.left) + dfs(node.right)
            self.values.append(value)
            return value
        else:
            return 0

    total = dfs(root)
    max_val = 0
    for val in self.values:
        max_val = max(max_val, (total - val) * val)

    return max_val % (10 ** 9 + 7)
