# https://leetcode.com/problems/my-calendar-i

class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect(self.intervals, (start, end))
        if idx > 0 and start < self.intervals[idx-1][1]:
            return False
        if idx < len(self.intervals) and end > self.intervals[idx][0]:
            return False
        bisect.insort(self.intervals, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)