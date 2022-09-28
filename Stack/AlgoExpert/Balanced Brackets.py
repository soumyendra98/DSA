# Stack implementation | O(N) and O(N)
def balancedBrackets(string):
    # Write your code here.
    stack = []
    opened = '{(['
    closed = '})]'
    oc_map = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for idx in range(len(string)):
        if string[idx] in opened:
            stack.append(string[idx])
        if string[idx] in closed:
            if len(stack) == 0 or stack[-1] != oc_map[string[idx]]:
                return False
            else:
                stack.pop()
        print(stack)
    return True if len(stack) == 0 else False
