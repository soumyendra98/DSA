# 150, Stack | O(N) and O(N)
from typing import List
def evalRPN(tokens: List[str]) -> int:
    operations = {"+", "-", "*", "/"}
    stack = []

    for char in tokens:
        if char not in operations:
            stack.append(int(char))
        else:
            if char == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 + val1)
            elif char == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif char == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 * val1)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))

    return stack.pop()
