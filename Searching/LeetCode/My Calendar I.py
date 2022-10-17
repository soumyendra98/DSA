# 729, Using Bisect to find the intersection | O(log(N)) and O(N)
import bisect


class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        if end <= start:
            return False

        right = bisect.bisect_right(self.calendar, start)
        left = bisect.bisect_left(self.calendar, end)

        if left % 2 or right % 2 or left != right:
            return False
        else:
            self.calendar[left:left] = (start, end)
            return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
