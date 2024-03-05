// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        N = len(nums)
        if N == 0:
            return 0
        L = [1 for _ in range(N)]
        for i in range(N):
            temp_max = 0
            for j in range(0,i):
                if nums[j] < nums[i]:
                    temp_max = max(temp_max, L[j])
            L[i] = temp_max + 1
        
        return max(L)