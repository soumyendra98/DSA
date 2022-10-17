# 112, Inorder Traversal | O(N) and O(H)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    output = [False]

    def dfs(node, curr_sum):
        if node is None:
            return

        curr_sum += node.val
        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
        if curr_sum == targetSum and node.left is None and node.right is None:
            output[0] = True
        curr_sum -= node.val

    dfs(root, 0)
    return output[0]
