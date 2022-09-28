# Using DFS(inorder) and Prefix Sum | O(N) and O(N)
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    output = [[]]

    def dfs(node, curr_sum, path):
        if node is None:
            return

        curr_sum += node.val
        path.append(node.val)

        dfs(node.left, curr_sum, path)
        dfs(node.right, curr_sum, path)

        if targetSum == curr_sum and (node.left is None and node.right is None):
            output[0].append(path[:])

        curr_sum -= path.pop()

    dfs(root, 0, [])

    return output[0]
