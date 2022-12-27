# 1554, Stack | O(N) and O(N)
def makeGood(s: str) -> str:
    s = list(s)
    stack = [s[0]]
    for i in range(1, len(s)):
        top = ''
        if len(stack):
            top = stack[-1]
        if top != s[i] and s[i].lower() == top.lower():
            stack.pop()
            continue
        stack.append(s[i])

    return "".join(stack)