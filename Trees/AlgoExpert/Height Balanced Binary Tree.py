# Using Height of binary Tree | O(N) and O(H)
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    # Write your code here.
    res = [True]

    def dfs(node):
        if node is None:
            return -1
        left = dfs(node.left)
        right = dfs(node.right)
        ans = max(left, right) + 1

        if abs(left - right) > 1:
            res[0] = False
        return ans

    dfs(tree)
    return res[0]
