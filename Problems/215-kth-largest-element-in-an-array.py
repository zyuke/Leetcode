# https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = sorted(nums, reverse=True)
        return s[k-1]