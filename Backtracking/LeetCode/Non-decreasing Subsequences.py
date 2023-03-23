# 495, Backtracking | O((2 ^ N) * (N ^ 2)) and ((2 ^ N) * N)
from typing import List


def findSubsequences(nums: List[int]) -> List[List[int]]:
    output = set()
    n = len(nums)

    def backtrack(arr, idx):
        for i, val in enumerate(nums[idx:]):
            if val >= arr[-1]:
                backtrack(arr + [val], idx + i + 1)
                output.add(tuple(arr[:] + [val]))

    for i in range(n - 1):
        backtrack([nums[i]], i + 1)

    return output
