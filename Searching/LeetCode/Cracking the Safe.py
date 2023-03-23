# 753, Using Hierholzers with permutaiton for edge creation | O(K! / N!) and O(K! / N!)

from collections import defaultdict
from itertools import product


def crackSafe(n: int, k: int) -> str:
    if n == 1:
        return "".join([str(i) for i in range(k)])

    graph = defaultdict(list)

    for edge in product(range(k), repeat=n):
        graph[tuple(edge[:-1])].append(tuple(edge[1:]))

    path = []

    def dfs(node):
        while graph[node]:
            dfs(graph[node].pop())
        path.append(str(node[0]))

    dfs(tuple([0] * (n - 1)))
    path = ['0' for _ in range(n - 2)] + path
    return "".join(path)
