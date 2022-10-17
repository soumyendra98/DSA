# Using Inorder Traversal | O(N) and O(H)
def nodeDepths(root):
    # Write your code here.
    total_depth = [0]

    def dfs(node, depth):
        if node is None:
            return
        total_depth[0] += depth
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
        depth -= 1

    dfs(root, 0)
    return total_depth[0]


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
