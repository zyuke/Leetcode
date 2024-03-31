class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        left, right, bad_idx = -1, -1, -1

        for i, n in enumerate(nums):
            if not minK <= n <= maxK:
                bad_idx = i
            if n == minK:
                left = i
            if n == maxK:
                right = i
            res += max(0, min(left, right) - bad_idx)

        return res

