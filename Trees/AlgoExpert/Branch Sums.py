# Using inorder traversal and prefix sum | O(N) and O(H)
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    output = []

    def dfs(node, curr_sum):
        if node is None:
            return
        curr_sum += node.value

        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
        if node.left is None and node.right is None:
            output.append(curr_sum)
        curr_sum -= node.value

    dfs(root, 0)
    return output
