# 49, Using Sorting | O(N) and O(N + log(K))
from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    index_map = defaultdict(list)
    output = []

    for idx, val in enumerate(strs):
        index_map["".join(sorted(val))].append(idx)

    for val in index_map.values():
        temp = []
        for idx in val:
            temp.append(strs[idx])
        output.append(temp)

    return output
