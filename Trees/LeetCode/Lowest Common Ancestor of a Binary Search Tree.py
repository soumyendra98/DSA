# 235, Tree Traversal and LCA | O(N) and O(N)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursive Solution
# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#     if root:
#         if not (root.left and root.right):
#             return root
#
#         if p.val < root.val and q.val > root.val:
#             return root
#         if q.val < root.val and p.val > root.val:
#             return root
#
#         if p.val == root.val:
#             return p
#         if q.val == root.val:
#             return q
#
#         if p.val < root.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#
#         if p.val > root.val:
#             return self.lowestCommonAncestor(root.right, p, q)


# Iterative solution (slower ?)
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while True:
        if root.val < p.val and root.val < q.val:
            root = root.right
        elif root.val > p.val and root.val > q.val:
            root = root.left
        else:
            return root