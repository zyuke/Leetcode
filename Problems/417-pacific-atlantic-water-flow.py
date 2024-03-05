// https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific_queue = []
        atlantic_queue = []
        
        def bfs(queue):
            connected = set()
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            while len(queue) > 0:
                (cur_x, cur_y) = queue.pop()
                connected.add((cur_x, cur_y))
                for (d_x, d_y) in directions:
                    new_x = cur_x + d_x
                    new_y = cur_y + d_y
                    if new_x >= 0 and new_x <= m-1 and new_y >= 0 and new_y <= n-1:
                        if (new_x, new_y) not in connected and heights[new_x][new_y] >= heights[cur_x][cur_y]:
                            queue.append((new_x, new_y))
            return connected
        
        for i in range(n):
            pacific_queue.append((0,i))
            atlantic_queue.append((m-1,i))
        for j in range(m):
            pacific_queue.append((j,0))
            atlantic_queue.append((j,n-1))
        
        pacific_connected = bfs(pacific_queue)
        atlantic_connected = bfs(atlantic_queue)
        
        return pacific_connected.intersection(atlantic_connected)