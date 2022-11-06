# 207,
from collections import defaultdict
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    p_map = defaultdict(list)
    for a, b in prerequisites:
        p_map[a].append(b)

    completed = set()
    cycle = [False]

    def dfs(idx, curr):
        if idx in completed:
            return
        if idx in curr:
            cycle[0] = True
            return
        if idx not in p_map:
            completed.add(idx)
            return

        curr.add(idx)

        for course in p_map[idx]:
            dfs(course, curr)

        completed.add(idx)

    for i in range(numCourses):
        if i not in completed:
            if i not in p_map:
                completed.add(i)
            else:
                dfs(i, set())
        if cycle[0]:
            return False

    return True
