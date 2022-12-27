# 2493, UF + BFS | O(N ^ 2) and O(N)
from collections import deque, defaultdict
from typing import List


def magnificentSets(n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    unionFind = {}

    def find(x):
        if x != unionFind[x]:
            unionFind[x] = find(unionFind[x])
        return unionFind[x]

    def union(x, y):
        unionFind.setdefault(x, x)
        unionFind.setdefault(y, y)
        unionFind[find(x)] = find(y)

    for node in range(1, n + 1):
        union(node, node)

    for x, y in edges:
        union(x, y)

    groups = defaultdict(list)

    for i in range(1, n + 1):
        groups[find(i)].append(i)

    def totalGroups(group):
        def bfs(nodes):
            q = deque()
            seen = set()
            for node in nodes:
                q.append(node)
                seen.add(node)
            level = 0
            while q:
                length = len(q)
                seen_b = set()
                for _ in range(length):
                    node = q.popleft()
                    seen_b.add(node)
                    for v in graph[node]:
                        if v in seen_b:
                            return -1
                        if v not in seen:
                            seen.add(v)
                            q.append(v)
                level += 1
            return level

        ans = -1

        for node in group:
            ans = max(ans, bfs([node]))

        return ans

    output = 0

    for g in groups:
        x = totalGroups(groups[g])
        if x == -1:
            return -1
        output += x

    return output
