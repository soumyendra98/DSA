# 1026, DFS | O(N) and O(logN)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    self.max_diff = -1

    def dfs(root, max_val, min_val):
        if not root:
            return

        if max_val < root.val:
            max_val = root.val
        if min_val > root.val:
            min_val = root.val

        self.max_diff = max(self.max_diff, max_val - min_val)

        dfs(root.left, max_val, min_val)
        dfs(root.right, max_val, min_val)

    dfs(root, root.val, root.val)
    return self.max_diff
