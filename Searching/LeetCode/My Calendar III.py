# 732, Using Bisect and maintain a frequency | O(N) and O(N)
import bisect


class MyCalendarThree:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> int:
        s = bisect.bisect_left(self.calendar, (start, 1))
        e = bisect.bisect_left(self.calendar, (end, -1))

        self.calendar.insert(s, (start, 1))
        self.calendar.insert(e + 1, (end, -1))

        total_bookings = 0
        max_bookings = 0
        for time, freq in self.calendar:
            total_bookings += freq
            if total_bookings > max_bookings:
                max_bookings = total_bookings

        return max_bookings

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
