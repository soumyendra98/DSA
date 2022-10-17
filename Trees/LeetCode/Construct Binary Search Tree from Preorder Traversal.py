# 1008, Using a Global Root to create the SubTrees | O(N) and O(N)
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    rootIndex = [0]

    def dfs(lowerBound, upperBound):
        root = rootIndex[0]

        if root >= len(preorder) or preorder[root] < lowerBound or preorder[root] >= upperBound:
            return None

        tree = TreeNode(preorder[root])

        rootIndex[0] += 1

        tree.left = dfs(lowerBound, tree.val)
        tree.right = dfs(tree.val, upperBound)

        return tree

    return dfs(float('-inf'), float('inf'))
