class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = res, res
        for i in range(1, len(nums)):
            if nums[i] < 0:
                curMin, curMax = curMax, curMin
            curMin = min(nums[i], curMin*nums[i])
            curMax = max(nums[i], curMax*nums[i])
            res = max(curMax, res)

        return res
