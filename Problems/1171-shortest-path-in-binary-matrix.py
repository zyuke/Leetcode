# https://leetcode.com/problems/shortest-path-in-binary-matrix

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == 1:
            return -1
        
        
        queue = [(0,0,1)]
        seen = set()
        direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        while queue:
            x, y, l = queue.pop(0)
            if x == m-1 and y == n-1:
                return l
            for d in direction:
                new_x, new_y = x+d[0], y+d[1]
                if 0<=new_x<=m-1 and 0<=new_y<=n-1 and (new_x, new_y) not in seen and grid[new_x][new_y] == 0:
                    seen.add((new_x, new_y))
                    queue.append((new_x, new_y,l+1))
        
        return -1
            
        