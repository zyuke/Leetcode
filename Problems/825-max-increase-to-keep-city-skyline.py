# https://leetcode.com/problems/max-increase-to-keep-city-skyline

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        vertical = []
        horizontal = [max(L) for L in grid]
        for i in range(n):
            col = [L[i] for L in grid]
            vertical.append(max(col))
        
        add = 0
        for i in range(m):
            for j in range(n):
                add += min(horizontal[i], vertical[j]) - grid[i][j]
        
        return add