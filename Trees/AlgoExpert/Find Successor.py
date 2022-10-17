# Inorder Traversal | O(H) and O(1)
# If Right Subtree Exists return its left most child
# Else find the next Parent

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    if node.right is not None:
        curr = node.right
        while True:
            if curr.left is not None:
                curr = curr.left
            else:
                return curr
    else:
        curr = node
        parent = node.parent
        while True:
            if parent is None:
                return None
            if curr == parent.left:
                return parent
            curr = parent
            parent = parent.parent
