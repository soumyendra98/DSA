# 300, Tabulation of the subproblem (arr[curr] > arr[bef]) and LIS[curr] > LIS[bef] + 1 | O(N^2) and O(N)
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    lis = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)

