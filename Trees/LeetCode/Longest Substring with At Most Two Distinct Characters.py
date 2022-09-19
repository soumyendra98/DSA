# 159, Two pointer and Hashmap | O(N) and O(1)
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    max_len = 0
    prev = ''
    curr = ''
    char_set = {}
    curr_len = 0

    for idx, val in enumerate(s):
        if len(char_set) < 2:
            if val not in char_set:
                char_set[val] = [idx, idx]
            else:
                char_set[val][1] = idx
            curr_len += 1
        else:
            if val not in char_set:
                curr_len = idx - max(char_set[curr][0], char_set[prev][1] + 1) + 1
                char_set.pop(prev)
                char_set[val] = [idx, idx]

            else:
                curr_len += 1
                char_set[val][1] = idx
        max_len = max(max_len, curr_len)
        if curr != val:
            prev, curr = curr, val
    return max_len

