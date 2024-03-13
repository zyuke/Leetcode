# https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = []
        for i in range(m):
            dp.append([0] * n)
        
        hori_ob = False
        for i in range(n):
            if hori_ob == False:
                if obstacleGrid[0][i] == 0:
                    dp[0][i] = 1
                else:
                    dp[0][i] = 0
                    hori_ob = True
            else:
                dp[0][i] = 0
                
        verti_ob = False
        for i in range(m):
            if verti_ob == False:
                if obstacleGrid[i][0] == 0:
                    dp[i][0] = 1
                else:
                    dp[i][0] = 0
                    verti_ob = True
            else:
                dp[i][0] = 0
                
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[m-1][n-1]