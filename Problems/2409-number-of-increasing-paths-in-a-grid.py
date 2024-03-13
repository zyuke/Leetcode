# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        dp = {}
        m = len(grid)
        n = len(grid[0])
        M = 1000000007
        
        def search(x,y):
            if (x,y) in dp:
                return dp[(x,y)]
            res = 1
            for d in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_x, new_y = x+d[0], y+d[1]
                if 0<=new_x<=m-1 and 0<=new_y<=n-1 and grid[x][y] < grid[new_x][new_y]:
                    res += search(new_x, new_y) % M
            
            dp[(x,y)] = res
            return res
        
        for i in range(m):
            for j in range(n):
                search(i,j)
        
        res = 0
        for p in dp:
            res = (res + dp[p]) % M
        return res                    