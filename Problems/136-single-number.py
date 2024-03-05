// https://leetcode.com/problems/single-number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for enum in nums:
            result = result^enum
        return result