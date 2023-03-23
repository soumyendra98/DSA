# 1519, DFS | O(26 * N) and O(26 * N)
from collections import defaultdict, Counter
from typing import List


def countSubTrees(n: int, edges: List[List[int]], labels: str) -> List[int]:
    tree = defaultdict(list)

    for x, y in edges:
        tree[x].append(y)
        tree[y].append(x)
    output = [0] * n

    def dfs(curr, prev):
        counts = Counter()
        for next_node in tree[curr]:
            if next_node != prev:
                counts += dfs(next_node, curr)

        counts[labels[curr]] += 1
        output[curr] = counts[labels[curr]]
        return counts

    dfs(0, 0)
    return output
