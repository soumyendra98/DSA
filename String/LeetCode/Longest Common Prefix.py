# Simple Matrix Traversal | O(N * M) and O(M)
from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    common = strs[0]
    idx = 0

    while idx < len(strs):
        for char_idx in range(min(len(strs[idx]), len(common))):
            if strs[idx][char_idx] != common[char_idx]:
                common = common[:char_idx]
                break
        if len(strs[idx]) < len(common):
            common = common[: len(strs[idx])]

        if common == '':
            return common
        idx += 1

    return common

