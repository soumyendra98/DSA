# 205, Hash Table | O(N) and O(N)

def isIsomorphic(s, t) -> bool:
    s_map = {}
    t_map = {}
    for i in range(len(s)):
        if s[i] in s_map:
            if s_map[s[i]] != t[i]:
                return False
        else:
            s_map[s[i]] = t[i]
            if t[i] in t_map:
                return False
            t_map[t[i]] = True
    return True


str1 = 'aff'
star2 = 'egg'
print(isIsomorphic(str1, star2))
