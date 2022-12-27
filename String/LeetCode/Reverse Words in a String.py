# 151, Single Pass | O(N) and O(1)
def reverseWords(s: str) -> str:
    s = s.split(" ")
    output = []
    for i in range(len(s) - 1, -1, -1):
        if s[i] != "":
            output.append(s[i])

    return " ".join(output)
