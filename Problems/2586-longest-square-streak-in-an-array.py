# https://leetcode.com/problems/longest-square-streak-in-an-array

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nset = set(nums)
        mct = -1
        for n in nums:
            ct = 1
            while n*n in nset:
                ct += 1
                n = n*n
            mct = max(mct, ct)
        return -1 if mct == 1 else mct