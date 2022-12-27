# 1207, Counter and Freq Set | O(N) and O(N)
from collections import Counter
from typing import List


def uniqueOccurrences(arr: List[int]) -> bool:
    num_count = Counter(arr)
    freq_set = set()
    for val in num_count.values():
        if val in freq_set:
            return False
        freq_set.add(val)

    return True
