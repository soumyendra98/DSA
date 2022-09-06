# 1448 Preorder Traversal | O(N) and O(N) as its recursive

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(self, root: TreeNode) -> int:
    if not root:
        return 0

    def preorder(node, max_val):
        if not node:
            return
        if node.val >= max_val:
            count[0] += 1
            max_val = node.val

        preorder(node.left, max_val)
        preorder(node.right, max_val)

    count = [0]
    preorder(root, root.val)
    return count[0]
