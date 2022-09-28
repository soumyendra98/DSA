# 199, Using BFS | O(N) and O(1)
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    output = []
    queue = deque([root])

    while len(queue) > 0:
        level = len(queue)
        while level > 0:
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if level == 1:
                output.append(node.val)
            level -= 1

    return output
