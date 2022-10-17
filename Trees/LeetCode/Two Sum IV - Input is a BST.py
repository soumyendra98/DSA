# 653, Simlpe DFS |O(N) and O(H)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTarget(root: Optional[TreeNode], k: int) -> bool:
    num_map = set()
    output = [False]

    def dfs(node):
        if node is None:
            return
        if (k - node.val) in num_map:
            output[0] = True
        num_map.add(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return output[0]
