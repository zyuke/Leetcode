from bisect import bisect_left
from functools import lru_cache

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        nodes = [(startTime[i], endTime[i], profit[i]) for i in range(N)]
        nodes.sort()
        startTime = [node[0] for node in nodes]

        @lru_cache(None)
        def dp(i):
            if i == N:
                return 0
            res = dp(i+1)
            j = bisect_left(startTime, nodes[i][1])
            res = max(res, dp(j)+nodes[i][2])
            return res

        return dp(0)

