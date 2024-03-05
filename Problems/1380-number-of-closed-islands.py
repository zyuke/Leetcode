// https://leetcode.com/problems/number-of-closed-islands

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def fill_edge(i, j):
            if grid[i][j] == 0:
                grid[i][j] = 1
                if i > 0:
                    fill_edge(i-1,j)
                if i < m-1:
                    fill_edge(i+1,j)
                if j > 0:
                    fill_edge(i,j-1)
                if j < n-1:
                    fill_edge(i,j+1)
        
        # fill the connected parts of edge with water
        for i in range(m):
            if grid[i][0] == 0:
                fill_edge(i,0)
            if grid[i][n-1] == 0:
                fill_edge(i,n-1)
        for j in range(n):
            if grid[0][j] == 0:
                fill_edge(0,j)
            if grid[m-1][j] == 0:
                fill_edge(m-1,j)
                
        def find_island(i, j):
            if grid[i][j] == 0:
                grid[i][j] = 1
                if i > 0:
                    fill_edge(i-1,j)
                if i < m-1:
                    fill_edge(i+1,j)
                if j > 0:
                    fill_edge(i,j-1)
                if j < n-1:
                    fill_edge(i,j+1)
        
        num_of_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    num_of_islands += 1
                    find_island(i, j)
        
        return num_of_islands