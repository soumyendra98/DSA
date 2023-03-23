# 352, Binary Seach | O(log(N)) and O(N)
from typing import List


class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.numbers = set()

    def addNum(self, value: int) -> None:
        if value in self.numbers:
            return
        self.numbers.add(value)
        l, r = 0, len(self.intervals)

        while l < r:
            mid = (l + r) // 2
            if self.intervals[mid][1] <= value:
                l = mid + 1
            else:
                r = mid
        if l - 1 >= 0 and self.intervals[l - 1][1] == value - 1:
            self.intervals[l - 1][1] = value
            if l < len(self.intervals) and self.intervals[l][0] == value + 1:
                self.intervals[l - 1][1] = self.intervals[l][1]
                self.intervals.pop(l)
        elif l < len(self.intervals) and self.intervals[l][0] == value + 1:
            self.intervals[l][0] = value
            if l - 1 >= 0 and self.intervals[l - 1][1] == value - 1:
                self.intervals[l][0] = self.intervals[l - 1][0]
                self.intervals.pop(l - 1)
        else:
            self.intervals.insert(l, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
