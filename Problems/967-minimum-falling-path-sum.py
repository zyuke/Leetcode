// https://leetcode.com/problems/minimum-falling-path-sum

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        N = len(A)
        table = [[0 for i in range(N+2)] for i in range(N)]
        
        for i in range(N):
            table[i][0] = 100000
            table[i][N+1] = 100000
            table[0][i+1] = A[0][i]
            
        for i in range(1,N):
            for j in range(1,N+1):
                table[i][j] = min(table[i-1][j-1:j+2]) + A[i][j-1]
            
        return min(table[N-1])