# 133, DFS | O(N) and O(N)

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return node

    clone = {
        node: Node(node.val)
    }
    stack = [node]
    visited = set()

    while stack:
        curr = stack.pop()

        if curr in visited:
            continue

        visited.add(curr)

        for next_node in curr.neighbors:
            if next_node not in clone:
                clone[next_node] = Node(next_node.val)
            stack.append(next_node)
            clone[curr].neighbors.append(clone[next_node])

    return clone[node]
