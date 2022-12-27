# 834, Postorder Traversal to calculate the sum for root and then
# preorder traversal to fill in the children | O(N) and O(N)

from collections import defaultdict
from typing import List


def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(set)
        subtrees = [1] * n
        sums = [0] * n

        for x, y in edges:
            tree[x].add(y)
            tree[y].add(x)

        def postOrder(root, prev):
            for node in tree[root]:
                if node != prev:
                    postOrder(node, root)
                    subtrees[root] += subtrees[node]
                    sums[root] += sums[node] + subtrees[node]

        def preOrder(root, prev):
            for node in tree[root]:
                if node != prev:
                    sums[node] = sums[root] + n - (2 * subtrees[node])
                    preOrder(node, root)

        postOrder(0, -1)
        preOrder(0, -1)
        return sums
