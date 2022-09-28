# 990, Using Union Find |O(N) and O(1)
from typing import List


def equationsPossible(equations: List[str]) -> bool:
    def find(i):
        if i != union[i]:
            union[i] = find(union[i])
        return union[i]

    union = {chr(x + 97): chr(x + 97) for x in range(26)}

    for val in equations:
        if val[1] == '=':
            union[find(val[0])] = find(val[3])
    for val in equations:
        if val[1] == "!" and find(val[0]) == find(val[3]):
            return False
    return True


