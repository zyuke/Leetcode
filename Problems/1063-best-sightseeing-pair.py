# https://leetcode.com/problems/best-sightseeing-pair

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [(0,0)] * len(values)
        dp[0] = (values[0], 0)
        cur_max = dp[0][0]
        for i in range(1, len(values)):
            if values[i] + dp[i-1][0] - i + dp[i-1][1] >= cur_max:
                cur_max = values[i] + dp[i-1][0] - i + dp[i-1][1]
            if values[i] >= dp[i-1][0] - i + dp[i-1][1]:
                dp[i] = (values[i], i)
            else:
                dp[i] = dp[i-1]
        
        return cur_max