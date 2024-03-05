// https://leetcode.com/problems/subarray-sum-equals-k

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        cum = 0
        
        cum_sum = {0 : 1}
        for i in range(len(nums)):
            cum += nums[i]
            if cum_sum.has_key(cum - k):
                count += cum_sum[cum - k]
            if cum_sum.has_key(cum):
                cum_sum[cum] += 1
            else:
                cum_sum[cum] = 1
                
        return count