// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        s_intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        
        to_app = s_intervals[0]
        for i in range(1, len(intervals)):
            if s_intervals[i][0] <= to_app[1]:
                to_app[1] = max(s_intervals[i][1], to_app[1])
            else:
                res.append(to_app)
                to_app = s_intervals[i]
        res.append(to_app)
        return res