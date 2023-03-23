# 2214, Maximum Value | O(N) and O(1)
from typing import List


def minimumHealth(damage: List[int], armor: int) -> int:
    max_val = 0
    total = 0
    for val in damage:
        if val > max_val:
            max_val = val
        total += val

    armor_reduction = armor if armor < max_val else max_val

    return total - armor_reduction + 1