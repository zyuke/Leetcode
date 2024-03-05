// https://leetcode.com/problems/wiggle-subsequence

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        pos_D = [1]*n
        neg_D = [1]*n
        for i in range(1,n):
            for j in range(0, i):
                if nums[i] > nums[j]:                   
                    pos_D[i] = max(pos_D[i], neg_D[j]+1)
                if nums[i] < nums[j]:
                    neg_D[i] = max(neg_D[i], pos_D[j]+1)
        
        return max(pos_D[n-1], neg_D[n-1])