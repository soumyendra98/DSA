# 437, Preorder Traversal + Prefix Sum | O(N) and O(N)
from collections import Counter
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    count = [0]
    nums = Counter([0])

    def dfs(node, curr_sum):
        if node is None:
            return

        curr_sum += node.val
        count[0] += nums[curr_sum - targetSum]
        nums[curr_sum] += 1

        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)

        # Removing the sum with the last node from counter
        nums[curr_sum] -= 1

    dfs(root, 0)

    return count[0]