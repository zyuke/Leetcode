// https://leetcode.com/problems/single-element-in-a-sorted-array

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res = res^i
            
        return res