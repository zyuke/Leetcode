// https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        subtotal = sum(nums)
        if subtotal < target:
            return 0 

        subtotal = 0
        i, j = 0, 0
        res = float('inf')
        while True:
            if subtotal >= target:
                res = min(res, j-i)
                subtotal -= nums[i]
                i += 1
            else:
                if j < len(nums):
                    subtotal += nums[j]
                    j += 1
                else:
                    break
        
        return res