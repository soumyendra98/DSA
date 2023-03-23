# 1129, BFS | O(M + N) and O(M + N)
from collections import defaultdict, deque
from typing import List


def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    graph_red = defaultdict(list)
    graph_blue = defaultdict(list)

    for a, b in redEdges:
        graph_red[a].append(b)

    for x, y in blueEdges:
        graph_blue[x].append(y)

    output = [-1] * n
    queue = deque([(0, 0), (0, 1)])
    visited = {0}
    distance = 0
    count = 0
    while queue:
        for _ in range(len(queue)):
            node, color = queue.popleft()

            if output[node] == -1:
                count += 1
                output[node] = distance

            if count == n:
                return output

            if color == 1:
                while graph_blue[node]:
                    next_node = graph_blue[node].pop()
                    queue.append((next_node, 0))
            else:
                while graph_red[node]:
                    next_node = graph_red[node].pop()
                    queue.append((next_node, 1))
        distance += 1
    return output
