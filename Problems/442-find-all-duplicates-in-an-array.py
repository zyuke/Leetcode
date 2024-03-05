// https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] *= -1
            else:
                res.append(abs(i))
                
        return res
        
    