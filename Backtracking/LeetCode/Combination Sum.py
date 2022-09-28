# 39, Using DFS to backtrack | O(N ^ 2) and O(N)
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    output = []

    def backtrack(arr, path, curr_target):
        if curr_target == 0:
            output.append(path)
            return
        if curr_target < 0:
            return
        for idx in range(len(arr)):
            backtrack(arr[idx:], path + [arr[idx]], curr_target - arr[idx])

    backtrack(candidates, [], target)

    return output
