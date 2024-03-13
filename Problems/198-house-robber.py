# https://leetcode.com/problems/house-robber

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        optm1 = max(nums[0], nums[1])
        optm2 = nums[0]
        opt = 0
        for i in range(2, n):
            opt = max(optm1, optm2 + nums[i])
            optm2 = optm1
            optm1 = opt
        return opt