# 101, Using BFS(Level Order Traversal) | O(N) and (2 ^ H) where H is the height of the Binary tree
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    if root.left is None and root.right is None:
        return True

    queue = deque([root])
    lot = []
    while len(queue) > 0:
        level = len(queue)
        temp = []
        while level > 0:
            node = queue.popleft()
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
                temp.append(node.val)
            else:
                temp.append(None)
            level -= 1
        left = 0
        right = len(temp) - 1
        while left <= right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
    return True
