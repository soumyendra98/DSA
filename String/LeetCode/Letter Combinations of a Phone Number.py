# 17, Hashmap | O(1) and O(1)
from collections import defaultdict
from typing import List


def letterCombinations(digits: str) -> List[str]:
    if len(digits) == 0:
        return []
    letter_map = defaultdict(list)
    char = 97
    for i in range(2, 7):
        for j in range(3):
            letter_map[str(i)].append(chr(char))
            char += 1
    letter_map['7'] = ['p', 'q', 'r', 's']
    letter_map['8'] = ['t', 'u', 'v']
    letter_map['9'] = ['w', 'x', 'y', 'z']
    output = ['']
    for digit in digits:
        temp = []
        for char in letter_map[digit]:
            for val in output:
                temp.append(val + char)
        output = temp
    return output
