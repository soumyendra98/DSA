# 409, Python Counter | O(N) and O(N)
from collections import Counter


def longestPalindrome(s: str) -> int:
    s_count = Counter(s)
    isOddAllowed = True
    max_len = 0
    for value in s_count.values():
        if value % 2 == 0:
            max_len += value
        else:
            if isOddAllowed:
                max_len += value
                isOddAllowed = False
            else:
                max_len += value - 1
    return max_len


string = "abccccddAA"
print(longestPalindrome(string))
