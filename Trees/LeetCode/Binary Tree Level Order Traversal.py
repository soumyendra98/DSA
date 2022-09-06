# 102, BFS | O(N) and O(M)


# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    output = []
    queue = [root]

    while len(queue) > 0:
        level = len(queue)
        temp = []
        while level != 0:
            node = queue.pop(0)
            temp.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            level -= 1
        output.append(temp)

    return output
