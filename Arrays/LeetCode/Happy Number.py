# Floyd's Cycle Detection | O(N) and O(1)


def nextValue(self, num: int) -> int:
    next_num = 0
    while num > 0:
        next_num += (num % 10) ** 2
        num = num // 10
    return next_num

def isHappy(self, n: int) -> bool:
    slow = n
    fast = self.nextValue(n)
    while fast != 1 and slow != fast:
        slow = self.nextValue(slow)
        fast = self.nextValue(self.nextValue(fast))

    return fast == 1

