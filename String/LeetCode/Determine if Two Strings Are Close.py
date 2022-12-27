# 1657, Counter | O(N) and O(N)
from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    count1 = Counter(word1)
    count2 = Counter(word2)

    if set(count1.keys()) == set(count1.keys()) & set(count2.keys()):
        return sorted(count1.values()) == sorted(count2.values())
    else:
        return False
