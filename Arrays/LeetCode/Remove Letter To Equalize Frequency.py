# 2423, Using Counter of Freq | O(N) and O(N)
from collections import Counter


def equalFrequency(word: str) -> bool:
    char_count = Counter(Counter(word).values())
    keys = list(char_count.keys())
    if len(char_count) == 1:
        return keys[0] == 1 or char_count[keys[0]] == 1
    if len(char_count) == 2:
        min_val, max_val = min(char_count.keys()), max(char_count.keys())
        return (min_val == 1 and char_count[min_val] == 1) or (int(max_val) == (int(min_val) + 1) and char_count[max_val] == 1)
    return False
