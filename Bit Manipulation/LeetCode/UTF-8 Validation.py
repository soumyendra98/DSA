# 393, Simple Significant Bit Check with given Conditions | O(N) and O(1)
from typing import List


def validUtf8(data: List[int]) -> bool:
    idx = 0
    bit_len = 0

    def countBits(num):
        count = 0
        idx= 7
        while idx >= 0:
            if (num & (1 << idx)) != 0:
                count += 1
            else:
                break
            idx -= 1
        return count

    while idx < len(data):
        if bit_len > 3:
            return False
        if bit_len != 0:
            if 128 <= data[idx] <= 191:
                bit_len -= 1
                idx += 1
            else:
                return False
        else:
            if data[idx] < 128:
                idx += 1
                continue
            elif data[idx] <= 191:
                return False
            else:
                bit_len += countBits(data[idx]) - 1
                idx += 1
    return (bit_len == 0)


