# Using DFS and Prefix Sum | O(N) and O(H)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:
    output = [-1000]

    def dfs(node):
        if node is None:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        output[0] = max(output[0], node.val + left + right)
        return max(left, right) + node.val

    dfs(root)
    return output[0]
