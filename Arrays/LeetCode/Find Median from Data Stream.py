# 295, Insertion Sort | O(N) and O(N)
from bisect import insort


class MedianFinder:

    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        insort(self.values, num)

    def findMedian(self) -> float:
        n = len(self.values)
        if n % 2 == 1:
            return self.values[n // 2]
        else:
            return (self.values[n // 2] + self.values[(n // 2) - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()