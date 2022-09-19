# 1457, Preorder Traversal with a Counter for path nodes |O(N) and O(K) where k is the max length of a path
from typing import Optional
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
    path_count = Counter()
    count = [0]

    def dfs(node):
        if node is None:
            return

        path_count[node.val] += 1

        dfs(node.left)
        dfs(node.right)

        if node.left is None and node.right is None:
            if checkPal():
                count[0] += 1

        path_count[node.val] -= 1

    def checkPal():
        flag = False

        for val in path_count.values():
            if flag and val % 2 != 0:
                return False
            if val % 2 != 0:
                flag = True
        return True

    dfs(root)
    return count[0]

