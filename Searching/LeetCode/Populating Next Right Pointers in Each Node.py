# 116, BFS | O(N) and O(log(N))
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return root

    queue = deque([root, None])

    while queue:
        level = len(queue) - 1
        while level:
            node = queue.popleft()
            node.next = queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level -= 1

        queue.popleft()
        if queue:
            queue.append(None)

    return root
