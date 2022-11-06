# 433, BFS on all genes | O(N) and O(N):
from collections import deque
from typing import List


def minMutation(start: str, end: str, bank: List[str]) -> int:
    bank = set(bank)
    n = len(start)
    if end not in bank:
        return -1

    gene_set = set(['A', 'C', 'G', 'T'])
    queue = deque([(start, 0)])
    idx = 0
    while queue:
        val, count = queue.popleft()
        if val == end:
            return count
        for idx in range(n):
            for char in gene_set:
                if val[idx] != char:
                    new_string = val[:idx] + char + val[idx + 1:]
                    if new_string in bank:
                        queue.append((new_string, count + 1))
    return -1
