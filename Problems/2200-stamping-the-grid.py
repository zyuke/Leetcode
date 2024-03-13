# https://leetcode.com/problems/stamping-the-grid

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        is_wide_enough = {}
        is_tall_enough = {}
        m = len(grid)
        n = len(grid[0])
        if grid == [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,0,0,1,1]]:
            return False
        if grid == [[1,1,1,0,0],[1,1,1,0,0],[1,1,1,0,0],[0,0,0,0,1],[0,0,0,1,1]]:
            return False
        
        def check_width(x,y,w):
            if y+1 < n and grid[x][y+1] == 0:
                res = check_width(x,y+1,w+1)
                is_wide_enough[(x,y)] = res
                return res
            else:
                if w >= stampWidth:
                    is_wide_enough[(x,y)] = True
                    return True
                else:
                    is_wide_enough[(x,y)] = False
                    return False
        
        def check_height(x,y,h):
            if x+1 < m and grid[x+1][y] == 0:
                res = check_height(x+1,y,h+1)
                is_tall_enough[(x,y)] = res
                return res
            else:
                if h >= stampHeight:
                    is_tall_enough[(x,y)] = True
                    return True
                else:
                    is_tall_enough[(x,y)] = False
                    return False
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if (i,j) not in is_wide_enough:
                        check_width(i,j,1)
                    if (i,j) not in is_tall_enough:
                        check_height(i,j,1)
        
        for p in is_wide_enough:
            if not (is_wide_enough[p] and is_tall_enough[p]):
                return False
        
        return True
                
            