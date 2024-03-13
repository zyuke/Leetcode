# https://leetcode.com/problems/array-partition

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        s_nums = sorted(nums)
        return sum(s_nums[2*i] for i in range(0, n))