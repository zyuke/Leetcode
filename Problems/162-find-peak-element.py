# https://leetcode.com/problems/find-peak-element

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i <= len(nums)-1:
            while i < len(nums)-1 and nums[i] < nums[i+1]:
                i += 1
            return i 