# 98, Inorder Traversal of BST | O(N) and O(N)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root, arr):

    if root is None:
        return
    inorder(root.left, arr)

    arr.append(root.val)

    inorder(root.right, arr)


def isValidBST(root: Optional[TreeNode]) -> bool:
    queue = []
    inorder(root, queue)
    for i in range(len(queue) - 1):
        if queue[i] >= queue[i + 1]:
            return False
    return True

