# 32, Using stack to find wrong indices | O(N) and O(N)
def longestValidParentheses(s: str) -> int:
    stack = [-1]
    for idx, val in enumerate(s):
        if val == '(':
            stack.append(idx)
        else:
            if len(stack) != 1 and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(idx)
    if len(stack) == 1:
        return len(s)

    end = len(s)
    max_len = 0
    for i in reversed(range(len(stack))):
        max_len = max(max_len, end - stack[i] - 1)
        end = stack[i]

    return max_len
