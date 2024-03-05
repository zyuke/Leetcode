// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return res
            