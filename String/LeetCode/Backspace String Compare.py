# Stack | O(N) and O(1)
def backspaceCompare(s: str, t: str) -> bool:
    if s == t:
        return True

    final_s = ""
    final_t = ""

    for idx in range(len(s)):
        if s[idx] == "#":
            final_s = final_s[:len(final_s) - 1]
        else:
            final_s += s[idx]

    for idx in range(len(t)):
        if t[idx] == "#":
            final_t = final_t[: len(final_t) - 1]
        else:
            final_t += t[idx]

    return final_s == final_t

