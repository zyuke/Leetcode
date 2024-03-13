# https://leetcode.com/problems/longest-continuous-increasing-subsequence

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        cur_ct = 1
        cur_max = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                cur_ct += 1
            else:
                cur_ct = 1
            cur_max = max(cur_max, cur_ct)
            
        return cur_max
                