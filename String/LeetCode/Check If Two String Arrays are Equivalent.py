# 1662, String Concatenation | O(N + M) and O(1)
from typing import List


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    str1 = "".join(word1)
    str2 = "".join(word2)
    return str1 == str2
