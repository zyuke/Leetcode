// https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        total, available = 0, 0
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        using = []
        
        for interval in sorted_intervals:
            while using and using[0] <= interval[0]:
                heapq.heappop(using)
                available += 1
            if available == 0:
                total += 1
            else:
                available -= 1
            heapq.heappush(using, interval[1])
            
        return total