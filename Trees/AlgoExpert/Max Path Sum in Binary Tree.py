# Using prefix sum of the subtrees | O(N) and O(H)
def maxPathSum(tree):
    # Write your code here.
    res = [float('-inf')]

    def dfs(node):
        if node is None:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)
        ans = max(left, right) + node.value
        res[0] = max(res[0], node.value + max(left, right, left + right))
        return ans

    dfs(tree)
    return res[0]


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

