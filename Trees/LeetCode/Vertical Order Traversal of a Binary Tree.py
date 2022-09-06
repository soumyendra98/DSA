# 987, DFS(PreOrder) | O(2^N) and O(2^N)
from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    h_d_dict = defaultdict(list)

    def preorder(node, h_d, v_d):
        if not node:
            return

        h_d_dict[h_d].append([v_d, node.val])

        if node.left:
            preorder(node.left, h_d - 1, v_d + 1)
        if node.right:
            preorder(node.right, h_d + 1, v_d + 1)

    preorder(root, 0, 0)

    return [
        [val for _, val in sorted(h_d_dict[key])]
        for key in sorted(h_d_dict)
    ]

