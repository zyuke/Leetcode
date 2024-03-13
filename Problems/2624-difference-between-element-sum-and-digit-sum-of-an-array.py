# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        e_sum = sum(nums)
        digits = []
        for n in nums:
            for d in str(n):
                digits.append(int(d))
        d_sum = sum(digits)
        return abs(e_sum - d_sum)