# Sorting Using Stack | O(N ^ 2) and O(N)
def sortStack(stack):
    # Write your code here.
    if len(stack) == 0:
        return stack
    top = stack.pop()
    sortStack(stack)

    sortStackHelper(stack, top)

    return stack


def sortStackHelper(stack, val):
    if len(stack) == 0 or stack[-1] <= val:
        stack.append(val)
        return

    top = stack.pop()

    sortStackHelper(stack, val)

    stack.append(top)