# 1061, Union Find | O(N * log(26)) and O(max(26, len(baseStr))

def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    n = len(s1)
    smallest_chars = {chr(i): chr(i) for i in range(97, 123)}
    used = [False] * 26

    def find(x):
        if x != smallest_chars[x]:
            smallest_chars[x] = find(smallest_chars[x])
        return smallest_chars[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx != ry:
            if rx > ry:
                smallest_chars[rx] = ry
            else:
                smallest_chars[ry] = rx

    for i in range(n):
        x, y = s1[i], s2[i]
        union(x, y)

    output = ''
    for char in baseStr:
        if used[ord(char) - 97]:
            output += smallest_chars[char]
        else:
            used[ord(char) - 97]
            output += find(char)

    return output
