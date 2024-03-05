// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        i, j = 0, n-1
        nums_sort = sorted(nums)
        t1 = t2 = 0
        while (nums_sort[i]+nums_sort[j]!=target):
            if nums_sort[i]+nums_sort[j] > target:
                j = j-1
            elif nums_sort[i]+nums_sort[j] < target:
                i += 1
        t1 = nums_sort[i]; t2 = nums_sort[j]
        
        for p in range(n):
            if nums[p] == t1:
                i = p
                break
        for q in range(n):
            if nums[n-1-q] == t2:
                j = n-1-q
                break
        return [i,j]
                