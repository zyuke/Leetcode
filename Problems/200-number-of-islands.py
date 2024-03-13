# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.grid = grid
        self.X = len(grid)
        self.Y = len(grid[0])
        res = 0
        
        for i in range(self.X):
            for j in range(self.Y):
                if self.grid[i][j] == '1':
                    self.dfs(i, j)
                    res += 1
                    
        return res
    
    def dfs(self, x, y):
        self.grid[x][y] = '0'
        if x > 0 and self.grid[x-1][y] == '1':
            self.dfs(x-1, y)
        if x < self.X - 1 and self.grid[x+1][y] == '1':
            self.dfs(x+1, y)
        if y < self.Y - 1 and self.grid[x][y+1] == '1':
            self.dfs(x, y+1)
        if y > 0 and self.grid[x][y-1] == '1':
            self.dfs(x, y-1)
            