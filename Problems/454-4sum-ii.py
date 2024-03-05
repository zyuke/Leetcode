// https://leetcode.com/problems/4sum-ii

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        N = len(A)
        AB = {}
        for i in range(N):
            for j in range(N):
                key = A[i] + B[j]
                try:
                    AB[key] += 1
                except:
                    AB[key] = 1
                    

        res = 0
        for i in range(N):
            for j in range(N):
                key = int(-1*(C[i]+D[j]))
                if key in AB:
                    res += AB[key]
                    
        return res