# 1136, Topological Sorting | O(N) and O(N)
from collections import defaultdict, deque
from typing import List


def minimumSemesters(n: int, relations: List[List[int]]) -> int:
    graph = defaultdict(set)
    indegree = defaultdict(int)

    for p, c in relations:
        graph[p].add(c)
        indegree[c] += 1

    queue = deque([i for i in range(1, n + 1) if i not in indegree])
    semesters = 0
    count = 0
    while queue:
        level = len(queue)
        while level:
            course = queue.popleft()
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
            count += 1
            level -= 1
        semesters += 1

    if count != n:
        return -1
    else:
        return semesters
