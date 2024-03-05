// https://leetcode.com/problems/best-team-with-no-conflicts

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [(age, score) for age, score in zip(ages, scores)]
        pairs.sort()
        n = len(ages)
        dp = [0]*n

        for i in range(n):
            dp[i] = pairs[i][1]
            for j in reversed(range(i)):
                if pairs[i][1] >= pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + pairs[i][1])

        return max(dp)