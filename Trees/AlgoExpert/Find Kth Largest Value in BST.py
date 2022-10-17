# Traversing from right - root - left | O(H + K) and O(H)
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    count = [0]

    def dfs(node):
        if node is None:
            return None
        right = dfs(node.right)
        if right is not None:
            return right
        count[0] += 1
        if count[0] == k:
            return node.value
        left = dfs(node.left)
        if left is not None:
            return left

    return dfs(tree)
