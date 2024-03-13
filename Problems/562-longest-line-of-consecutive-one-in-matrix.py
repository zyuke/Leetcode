# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = []
        for i in range(m):
            new_row = []
            for j in range(n):
                new_row.append([0]*4)
            dp.append(new_row)
        
        directions = [[0,-1],[-1,-1],[-1,0],[-1,1]]
        res = 0
        for i in range(m):
            for j in range(n):
                for r, d in enumerate(directions):
                    prev_i, prev_j = i+d[0], j+d[1]
                    if 0<=prev_i<=m-1 and 0<=prev_j<=n-1:
                        if mat[i][j] == 1:
                            dp[i][j][r] = dp[prev_i][prev_j][r] + 1
                        else:
                            dp[i][j][r] = 0
                    else:
                        dp[i][j][r] = int(mat[i][j] == 1)
                    res = max(res, dp[i][j][r])
        
        return res