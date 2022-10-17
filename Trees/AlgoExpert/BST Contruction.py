# BST Implementation | O(log(N)) and O(log(N))

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        node = self
        while True:
            if node.value > value:
                if node.left is None:
                    node.left = BST(value)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = BST(value)
                    break
                else:
                    node = node.right

        return self

    def contains(self, value):
        # Write your code here.
        node = self
        while node is not None:
            if node.value == value:
                return True
            elif node.value > value:
                node = node.left
            else:
                node = node.right
        return False

    def totalNodes(self, node):
        if node is None:
            return 0
        count = 0
        queue = [node]
        while len(queue) > 0:
            level = len(queue)
            while level > 0:
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                count += 1
                level -= 1
        return count

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        node = self
        prev = None
        while True:
            if node.value < value:
                prev = node
                node = node.right
            elif node.value > value:
                prev = node
                node = node.left
            else:
                while node.right is not None and node.right.value == node.value:
                    prev = node
                    node = node.right
                left_count = self.totalNodes(node.left)
                right_count = self.totalNodes(node.right)
                if left_count > right_count:
                    left = node.left
                    curr = left.right
                    if curr is None:
                        node.value = left.value
                        node.left = left.left
                        return self
                    while curr.right is not None:
                        left = curr
                        curr = curr.right
                    node.value = curr.value
                    if curr.left is not None:
                        left.right = curr.left
                    else:
                        left.right = None
                else:
                    if node.right is None:
                        if prev is not None:
                            if node.value < prev.value:
                                prev.left = None
                            else:
                                prev.right = None
                            return self
                        else:
                            return None
                    right = node.right
                    curr = right.left
                    if curr is None:
                        node.value = right.value
                        node.right = right.right
                        return self
                    while curr.left is not None:
                        right = curr
                        curr = curr.left
                    node.value = curr.value
                    if curr.right is not None:
                        right.left = curr.right
                    else:
                        right.left = None
                return self

        return self
