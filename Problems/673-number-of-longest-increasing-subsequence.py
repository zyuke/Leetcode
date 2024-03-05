// https://leetcode.com/problems/number-of-longest-increasing-subsequence

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if not N:
            return 0
        dp1, dp2 = [1] * N, [1] * N
        maxlen, count = 1, 1
        
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp1[j] + 1 > dp1[i]:
                        dp1[i] = dp1[j] + 1
                        dp2[i] = dp2[j]
                    elif dp1[j] + 1 == dp1[i]:
                        dp2[i] += dp2[j]
                    
            if maxlen < dp1[i]:
                maxlen = dp1[i]
                count = dp2[i]
            elif maxlen == dp1[i]:
                count += dp2[i]
                
        return count
            