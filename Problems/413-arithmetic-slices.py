// https://leetcode.com/problems/arithmetic-slices

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        if N <= 2:
            return 0
        
        count = 0
        streak = 0
        for i in range(2, N):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                streak += 1
                count += streak
            else:
                streak = 0
        
        return count