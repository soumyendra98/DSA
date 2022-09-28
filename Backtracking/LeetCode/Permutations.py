# 46, Using DFS | O(N ^ 2) and O(N)
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    output = []

    def backtrack(arr, path):
        if len(arr) == 1:
            output.append(path + arr)
            return
        for idx in range(len(arr)):
            backtrack(arr[:idx] + arr[idx + 1:], path + [arr[idx]])

    backtrack(nums, [])

    return output
