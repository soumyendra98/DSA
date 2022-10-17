# Using binary search to find the Roots of subtrees | O(N) and O(N)
def minHeightBst(array):
    left = 0
    right = len(array) - 1

    def create(left, right):
        if left <= right:
            mid = (left + right) // 2
            node = BST(array[mid])
            node.left = create(left, mid - 1)
            node.right = create(mid + 1, right)
            return node

    return create(left, right)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
