# Stack with circular index | O(N) and O(N)
def nextGreaterElement(array):
    # Write your code here.
    output = [-1] * len(array)
    stack = []
    for i in reversed(range(2 * len(array))):
        circ = i % len(array)
        while len(stack) > 0:
            if stack[-1] <= array[circ]:
                stack.pop()
            else:
                output[circ] = stack[-1]
                break
        stack.append(array[circ])

    return output
