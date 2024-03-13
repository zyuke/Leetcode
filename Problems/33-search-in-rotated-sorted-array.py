# https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, x in enumerate(nums):
            if x == target:
                return i
        
        return -1
        