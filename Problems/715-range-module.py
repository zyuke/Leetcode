# https://leetcode.com/problems/range-module

class RangeModule:

    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        left_idx = bisect.bisect_left(self.track, left)
        right_idx = bisect.bisect_right(self.track,right)
        interval = []
        if left_idx % 2 == 0:
            interval.append(left)
        if right_idx % 2 == 0:
            interval.append(right)
        self.track[left_idx:right_idx] = interval
        

    def queryRange(self, left: int, right: int) -> bool:
        left_idx = bisect.bisect_right(self.track,left)
        right_idx = bisect.bisect_left(self.track,right)
        return left_idx == right_idx and right_idx %2 == 1

    def removeRange(self, left: int, right: int) -> None:
        left_idx = bisect.bisect_left(self.track,left)
        right_idx = bisect.bisect_right(self.track,right)
        interval = []
        if left_idx % 2 == 1:
            interval.append(left)
        if right_idx % 2 == 1:
            interval.append(right)
        self.track[left_idx:right_idx] = interval

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)