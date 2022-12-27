# 1704, Hashmap | O(N) and O(1)

def halvesAreAlike(s: str) -> bool:
    n = len(s)
    m = n // 2
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count_1 = count_2 = 0

    for i in range(m):
        if s[i] in vowels:
            count_1 += 1
        if s[i + m] in vowels:
            count_2 += 1

    return count_1 == count_2
