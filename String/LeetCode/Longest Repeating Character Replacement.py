# 424, Hash Table and Sliding Window | O(N) and O(1)
def characterReplacement(s: str, k: int) -> int:
    char_count = {}
    start = 0
    max_len = 0
    for idx, val in enumerate(s):

        if val in char_count:
            char_count[val] += 1
        else:
            char_count[val] = 1

        if idx - start + 1 - max(char_count.values()) > k:
            start += 1
            char_count[s[start - 1]] -= 1

        max_len = max(max_len, idx - start + 1)

    return max_len


str1 = 'ABAA'
print(characterReplacement(str1, 1))