// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Nnums = [i for i in range(1,len(nums)+1)]
        SN = set(Nnums)
        return list(SN-set(nums))