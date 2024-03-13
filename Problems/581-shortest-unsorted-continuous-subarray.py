# https://leetcode.com/problems/shortest-unsorted-continuous-subarray

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st_nums = sorted(nums)
        if st_nums == nums:
            return 0
        
        i = 0
        j = len(nums) - 1
        
        while nums[i] == st_nums[i] and i <= j:
            i += 1
        while nums[j] == st_nums[j] and j >= i:
            j -= 1
            
        return j - i + 1