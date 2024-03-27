class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0 
        N = len(nums)
        prod = 1

        for right in range(N):
            prod *= nums[right]
            while left <= right and prod >= k:
                prod /= nums[left]
                left += 1
            res += right - left + 1

        return res
