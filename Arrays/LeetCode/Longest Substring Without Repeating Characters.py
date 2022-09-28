# 3, HashMap | O(N) and O(1)
def lengthOfLongestSubstring(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    char_dict = {}
    start = 0
    max_len = 0

    for idx, val in enumerate(s):
        if val not in char_dict:
            char_dict[val] = idx

        else:
            start = max(char_dict[val] + 1, start)
            char_dict[val] = idx

        max_len = max(idx - start + 1, max_len)
    return max(max_len, idx - start)
