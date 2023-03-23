# 93, Simple Backtracking | O((M ^ N) * N) and O((M ^ N) * N) where N is the segments and M is the no of digits in each
# segment. In this question M = 3 and N = 4 and hence the complexities are O(1) and O(1)
from typing import List

def restoreIpAddresses(s: str) -> List[str]:
    n = len(s)

    if n > 12 or n < 4:
        return []

    output = []

    def backtrack(curr, idx, dots):
        if dots == 4 and idx == n:
            output.append(".".join(curr))

        if idx >= n:
            return

        if s[idx] == '0':
            backtrack(curr + [s[idx: idx + 1]], idx + 1, dots + 1)
        else:
            for i in range(idx, min(n, idx + 3)):
                if int(s[idx: i + 1]) < 256:
                    backtrack(curr + [s[idx: i + 1]], i + 1, dots + 1)

    backtrack([], 0, 0)
    return output
