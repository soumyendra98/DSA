# 155, Maintaining a Stack for the current minimum | O(1) and O(N)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val
        self.min_stack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if len(self.min_stack) == 0:
            self.min = float('inf')
            return
        self.min = self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
