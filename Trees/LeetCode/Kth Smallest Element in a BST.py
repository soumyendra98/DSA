# 230, Inorder Traversal | O(N) and O(N)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []

    def inorder(node):
        if node is None:
            return
        if len(stack) > k:
            return
        inorder(node.left)
        stack.append(node.val)
        inorder(node.right)

    inorder(root)
    return stack[k - 1]
