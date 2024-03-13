# https://leetcode.com/problems/minimum-time-difference

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for t in timePoints:
            minutes.append(int(t[:2])*60+int(t[-2:]))
        res = 1441
        minutes.sort()
        for i in range(len(minutes)-1):
            res = min(res, minutes[i+1]-minutes[i])
        res = min(res, 1440+minutes[0]-minutes[-1])
        return res