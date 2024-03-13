# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        
        for n in nums:
            cur_len = 1
            small = n-1
            large = n+1
            while small in num_set:
                cur_len += 1
                num_set.remove(small)
                small -= 1
            while large in num_set:
                cur_len += 1
                num_set.remove(large)
                large += 1
            
            if cur_len > res:
                res = cur_len
        
        return res