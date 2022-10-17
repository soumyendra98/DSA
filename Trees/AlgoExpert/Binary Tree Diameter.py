# Using DFS to calculate Left and Right Height | O(N) and O(H)
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    longest_path = [0]

    def dfs(node):
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        curr_path = left + right
        longest_path[0] = max(longest_path[0], curr_path)
        return max(left, right) + 1

    dfs(tree)
    return longest_path[0]
