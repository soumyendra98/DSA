# 451, Hashmap and Sorting | O(NlogN) and O(N)

from collections import Counter


def frequencySort(s: str) -> str:
    char_count = Counter(s)

    char_list = sorted(char_count.items(), key=lambda x: -x[1])

    output = ""

    for char, count in char_list:
        output += char * count
    return output
