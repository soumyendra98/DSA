# Level Order Traversal using queue | O(N) and O(N-1 == N) where N is the total no nodes
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root: 'Node') -> List[List[int]]:
    if not root:
        return []

    output = []
    queue = [root]

    while len(queue) != 0:
        level = len(queue)
        temp = []

        while level != 0:
            node = queue.pop(0)
            temp.append(node.val)

            for child in node.children:
                queue.append(child)

            level -= 1
        output.append(temp)
    return output


