# https://leetcode.com/problems/missing-number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n*(n+1)/2
        total_l = sum(nums)
        return total - total_l