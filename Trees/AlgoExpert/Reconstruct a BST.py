# Using a global Root to form the subtrees | O(N) and O(N)
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    rootIndex = [0]

    def dfs(lowerBound, upperBound):
        index = rootIndex[0]
        if index >= len(preOrderTraversalValues) or preOrderTraversalValues[index] < lowerBound or preOrderTraversalValues[index] >= upperBound:
            return None
        tree = BST(preOrderTraversalValues[index])
        rootIndex[0] += 1
        tree.left = dfs(lowerBound, tree.value)
        tree.right = dfs(tree.value, upperBound)

        return tree

    root = dfs(float('-inf'), float('inf'))
    return root
