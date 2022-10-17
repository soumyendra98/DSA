# 731, Using Bisect and maintain a frequency | O(N) and O(N)
import bisect


class MyCalendarTwo:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        s = bisect.bisect_left(self.calendar, (start, 1))
        e = bisect.bisect_left(self.calendar, (end, -1))
        bookings = 0

        for time, freq in self.calendar[:s]:
            bookings += freq

        if bookings == 2:
            return False
        for time, freq in self.calendar[s:e]:
            bookings += freq
            if bookings == 2:
                return False

        self.calendar.insert(s, (start, 1))
        self.calendar.insert(e + 1, (end, -1))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
