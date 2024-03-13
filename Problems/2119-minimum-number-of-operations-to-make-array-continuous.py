# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        nums = sorted(set(nums))
        for i, start in enumerate(nums):
            end = start + n - 1
            idx = bisect_right(nums, end)
            uniqueLen = idx - i
            res = min(res, n - uniqueLen)
        
        return res