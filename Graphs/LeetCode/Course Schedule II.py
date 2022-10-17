# 210, DFS on each prerequisites | O(N * H) and O(H) where H is the max no of prerequisites for a course
from collections import defaultdict
from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    p_map = defaultdict(list)

    for a, b in prerequisites:
        p_map[a].append(b)

    completed = {}
    cycle = [False]

    def dfs(idx, curr):
        if idx in completed:
            return

        if idx in curr:
            print(idx, curr)
            cycle[0] = True
            return

        if idx not in p_map:
            completed[idx] = None
            return

        curr.add(idx)

        for val in p_map[idx]:
            dfs(val, curr)
        completed[idx] = None

    for i in range(numCourses):
        if i not in completed:
            if i not in p_map:
                completed[i] = None
            else:
                dfs(i, set())
        if cycle[0]:
            return []

    return list(completed.keys())
