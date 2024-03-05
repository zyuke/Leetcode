// https://leetcode.com/problems/swim-in-rising-water

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = [(grid[0][0],0,0)]
        seen = set()
        res = 0
        
        while queue:
            d, x, y = heapq.heappop(queue)
            res = max(res, d)
            if x == N-1 and y == N-1:
                return res
            for (new_x, new_y) in [(x-1,y), (x+1, y), (x,y+1),(x,y-1)]:
                if 0 <= new_x <= N-1 and 0 <= new_y <= N-1 and (new_x, new_y) not in seen:
                    heapq.heappush(queue, (grid[new_x][new_y], new_x, new_y))
                    seen.add((new_x, new_y))