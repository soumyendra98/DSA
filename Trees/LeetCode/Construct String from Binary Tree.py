# Preorder Traversal | O(N) and O(N)
from typing import Optional


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree2str(self, root: Optional[TreeNode]) -> str:
    output = [""]

    def preorder(node):
        if node is not None:
            output[0] += str(node.val)

            if node.left:
                output[0] += '('
                preorder(node.left)
                output[0] += ')'

            if node.right:
                if node.left is None:
                    output[0] += '()'
                output[0] += '('
                preorder(node.right)
                output[0] += ')'

    preorder(root)
    return output[0]