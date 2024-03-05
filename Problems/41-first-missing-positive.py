// https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        i = 1
        while True:
            if i in num_set:
                i += 1
            else:
                return i