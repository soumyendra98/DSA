# Using Bounds for BST | O(N) and O(H)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min_val=float('-inf'), max_val=float('inf')):
    # Write your code here.
    if tree is None:
        return True
    if not min_val <= tree.value <= max_val:
        return False

    return validateBst(tree.left, min_val, tree.value - 1) and validateBst(tree.right, tree.value, max_val)
