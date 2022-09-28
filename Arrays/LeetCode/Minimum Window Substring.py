# 76, Using Counter and Sliding Window | O(N ^ 2) and O(T) where T is the length of string t.
from collections import Counter


def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ''

    t_count = Counter(t)
    window = len(t_count)
    curr_count = 0
    start = 0
    end = 0
    sol = ()

    while end < len(s):
        if s[end] in t_count:
            t_count[s[end]] -= 1
            if t_count[s[end]] == 0:
                curr_count += 1

        while start <= end and curr_count == window:
            if s[start] in t_count:
                t_count[s[start]] += 1

            if t_count[s[start]] > 0:
                if len(sol) == 0:
                    sol = (start, end + 1)
                elif sol[1] - sol[0] > end - start + 1:
                    sol = (start, end + 1)
                curr_count -= 1
            start += 1

        end += 1

    return s[sol[0]: sol[1]] if len(sol) > 0 else ''
