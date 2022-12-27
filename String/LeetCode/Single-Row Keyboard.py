# 1165, Hashmap | O(N) and O(1)
def calculateTime(keyboard: str, word: str) -> int:
    char_map = {}
    for i in range(len(keyboard)):
        char_map[keyboard[i]] = i

    total = 0
    idx = 0
    for char in word:
        total += abs(idx - char_map[char])
        idx = char_map[char]
    return total
