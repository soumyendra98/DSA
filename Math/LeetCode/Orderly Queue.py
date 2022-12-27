# 899, if k is one then min of all rotations else sorting | O(N^2) and O(1)

def orderlyQueue(s: str, k: int) -> str:
    n = len(s)
    if k == 1:
        min_val = s
        for i in range(1, n):
            if s[i:] + s[:i] < min_val:
                min_val = s[i:] + s[:i]
        return min_val
    else:
        return "".join(sorted(s))
