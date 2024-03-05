// https://leetcode.com/problems/peak-index-in-a-mountain-array

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_pos = 0
        max_val = 0
        
        
        for i in range(1,len(A)):
            if A[i] > max_val:
                max_val = A[i]
                max_pos = i
                
        return max_pos