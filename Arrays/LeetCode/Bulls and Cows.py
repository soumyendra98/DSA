# 299, Hash Table | O(N) and O(1)
from collections import Counter


def getHint(secret: str, guess: str) -> str:
    sec_count = Counter(secret)
    gue_count = Counter(guess)
    output = [0, 0]

    for key in sec_count.keys():
        if key in gue_count:
            if gue_count[key] <= sec_count[key]:
                output[1] += gue_count[key]
            else:
                output[1] += sec_count[key]

    for idx, val in enumerate(guess):
        if val == secret[idx]:
            output[0] += 1
            output[1] -= 1

    return str(output[0]) + "A" + str(output[1]) + "B"

