// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        cur_sum = nums[0] + nums[1]
        res = -1
        for i in range(2, len(nums)):
            if cur_sum > nums[i]:
                cur_sum += nums[i]
                res = cur_sum
            else:
                cur_sum += nums[i]
        return res