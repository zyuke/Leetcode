class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res, earlist_end = 0, -float('inf')
        intervals.sort(key=lambda x: x[1])
        for start, end in intervals:
            if start >= earlist_end:
                earlist_end = end
            else:
                res += 1
        return res
        
