# Topological Sorting
from collections import deque,defaultdict


class Khans:
    def __int__(self, edges, n):
        output = []
        graph = defaultdict(set)
        in_degree = defaultdict(int)

        for a, b in edges:
            graph[b].add(a)
            in_degree[a] += 1

        queue = deque([i for i in range(n) if i not in in_degree])
        count = 0
        while queue:
            node = queue.popleft()
            output.append(node)

            for next_node in graph[node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)

            count += 1
        if count != n:
            return []

        return output
