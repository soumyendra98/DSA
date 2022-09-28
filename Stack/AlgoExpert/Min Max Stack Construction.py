# Maintaining a Min and a Max Stack | O(1) and O(1)
class MinMaxStack:
    def __init__(self):
        self.min = float('inf')
        self.max = float('-inf')
        self.stack = []
        self.max_stack = []
        self.min_stack = []

    def peek(self):
        # Write your code here.
        if len(self.stack) == 0:
            return "Empty"
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        if len(self.stack) == 1:
            self.min = float('inf')
            self.max = float('-inf')
            self.max_stack = []
            self.min_stack = []
        else:
            self.min_stack.pop()
            self.min = self.min_stack[-1]
            self.max_stack.pop()
            self.max = self.max_stack[-1]
        return self.stack.pop()

    def push(self, number):
        # Write your code here.
        self.stack.append(number)
        self.min = min(self.min, number)
        self.max = max(self.max, number)
        self.min_stack.append(self.min)
        self.max_stack.append(self.max)

    def getMin(self):
        # Write your code here.
        return self.min
