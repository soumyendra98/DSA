# 131, Backtracking | O( N * 2 ^ N) and O(N)
from typing import List
def partition(s: str) -> List[List[str]]:
    n = len(s)
    output = []

    def backtrack(path, idx):
        if idx == n:
            output.append(path)
            return
        for i in range(idx, n):
            val = s[idx: i + 1]
            if val == val[::-1]:
                backtrack(path + [val], i + 1)

    backtrack([], 0)
    return output
