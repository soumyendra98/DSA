# Using Sorting and Hash Map | O(NlogN) and O(N)
from collections import defaultdict
from typing import List


def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
    if len(properties) < 2:
        return 0

    attack_dict = defaultdict(list)

    properties.sort(key=lambda x: x[0])

    for val in properties:
        attack_dict[val[0]].append(val[1])

    max_def = 0
    count = 0

    for i in reversed(attack_dict.keys()):
        for val in attack_dict[i]:
            if val < max_def:
                count += 1
        max_def = max(max_def, max(attack_dict[i]))

    return count

