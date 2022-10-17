# Simple DFS | O(log(N)) and O(log(N))
def findClosestValueInBst(tree, target):
    # Write your code here.
    dist = [(float('inf'), 0)]

    def dfs(node):
        if node is None:
            return
        diff = abs(node.value - target)
        if diff < dist[0][0]:
            dist[0] = (diff, node.value)
        if node.value > target:
            dfs(node.left)
        elif node.value < target:
            dfs(node.right)
        else:
            return node.value

    dfs(tree)
    return dist[0][1]


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
