// https://leetcode.com/problems/remove-covered-intervals

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        cur_max_right = -1
        res = len(intervals)
        for (x,y) in intervals:
            if y <= cur_max_right:
                res -= 1
            cur_max_right= max(cur_max_right, y)

        return res