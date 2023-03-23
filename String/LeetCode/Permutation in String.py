# 567, Hashmap + Sliding window | O(N) and O(1)
from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    count1 = Counter(s1)
    count2 = Counter(s2[:len(s1)])
    j = 0
    for i in range(len(s1), len(s2)):
        if count1 == count2:
            return True
        count2[s2[i]] += 1
        count2[s2[j]] -= 1
        j += 1

    return False
