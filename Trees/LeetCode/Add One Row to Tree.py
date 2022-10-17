# 623, Using DFS | O(N) and O(H)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
        return TreeNode(val, root, None)
    findDepth(root, 1, val, depth)
    return root

def findDepth(root, cur_depth, val, depth):
    if not root: return
    if cur_depth == depth - 1:
        root.left = TreeNode(val, root.left, None)
        root.right = TreeNode(val, None, root.right)
    else:
        findDepth(root.left, cur_depth + 1, val, depth)
        findDepth(root.right, cur_depth + 1, val, depth)
