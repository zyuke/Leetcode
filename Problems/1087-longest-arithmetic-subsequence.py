# https://leetcode.com/problems/longest-arithmetic-subsequence

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        DP = dict()
        n = len(nums)
        for i in range(1, n):
            for j in range(0, i):
                d = nums[i] - nums[j]
                if (j,d) in DP:
                    DP[(i,d)] = DP[(j,d)] + 1
                else:
                    DP[(i,d)] = 2
            
        return max(DP.values())