# 637, Level Order Traversal | O(N) and O(N)
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []

    output = []
    queue = [root]

    while len(queue) != 0:
        level = len(queue)
        count = len(queue)
        level_sum = 0
        while level > 0:
            node = queue.pop(0)
            level_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            level -= 1

        output.append(level_sum / count)

    return output

