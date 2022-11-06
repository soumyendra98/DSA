# 1239, Set Intersection and Union | O(2 ^ N) and O(2 ^ min(N, K)) where K is the no of unique characters in the array
from typing import List


def maxLength(arr: List[str]) -> int:
    max_len = 0
    dp = [set()]
    for val in arr:
        val_set = set(val)
        if len(val_set) != len(val):
            continue
        for item in dp:
            if len(item & val_set) == 0:
                dp.append(item | val_set)
                if len(item | val_set) > max_len:
                    max_len = len(item | val_set)
    return max_len
