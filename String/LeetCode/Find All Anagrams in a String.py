# 438,
from collections import Counter
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    if len(s) < len(p):
        return []

    output = []
    count_p = Counter(p)
    count_s = {}
    for idx in range(len(s)):

        if s[idx] in count_p:
            if s[idx] in count_s:
                count_s[s[idx]] += 1
            else:
                count_s[s[idx]] = 1

        if idx > len(p) - 1 and s[idx - len(p)] in count_s:
            count_s[s[idx - len(p)]] -= 1

        if count_s == count_p:
            output.append(idx - len(p) + 1)

    return output


str1 = 'ab'
str2 = 'abab'

print(findAnagrams(str2, str1))
