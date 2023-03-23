# 1631, SPFA | O(E * V) and O(V)
from collections import defaultdict, deque
from typing import List


def minimumEffortPath(heights: List[List[int]]) -> int:
    M = len(heights)
    N = len(heights[0])

    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    distances = defaultdict(lambda: float('inf'))
    queue = deque([(0, 0)])
    distances[(0, 0)] = 0

    while queue:
        r, c = queue.popleft()

        for x, y in directions:
            if 0 <= r + x < M and 0 <= c + y < N:
                next_weight = max(abs(heights[r][c] - heights[r + x][c + y]), distances[(r, c)])
                if distances[(r + x, c + y)] > next_weight:
                    distances[(r + x, c + y)] = next_weight
                    queue.append((r + x, c + y))

    return distances[(M - 1, N - 1)]

# Dijkstra's

    # M = len(heights)
    # N = len(heights[0])
    #
    # directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    # distances = [[float('inf')] * N for _ in range(M)]
    #
    # heap = [(0, 0, 0)]
    #
    # while heap:
    #     weight, x, y = heappop(heap)
    #
    #     if x == M - 1 and y == N - 1:
    #         return weight
    #
    #     for i, j in directions:
    #         r, c = x + i, y + j
    #         if 0 <= r < M and 0 <= c < N:
    #             next_weight = max(weight, abs(heights[x][y] - heights[r][c]))
    #             if distances[r][c] > next_weight:
    #                 distances[r][c] = next_weight
    #                 heappush(heap, (next_weight, r, c))
    # return -1