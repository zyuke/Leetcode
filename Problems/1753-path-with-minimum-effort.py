// https://leetcode.com/problems/path-with-minimum-effort

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        
        def checkPath(cutoff):
            queue = [(0,0)]
            visited = set([(0,0)])
            while queue:
                cur_x, cur_y = queue.pop(0)
                if cur_x == m-1 and cur_y == n-1:
                    return True
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    new_x, new_y = cur_x + dx, cur_y + dy
                    if 0<=new_x<=m-1 and 0<=new_y<=n-1 and (new_x, new_y) not in visited:
                        if abs(heights[new_x][new_y]-heights[cur_x][cur_y]) <= cutoff:
                            queue.append((new_x, new_y))
                            visited.add((new_x, new_y))
            
            return False
        
        low, high = 0, 1000000
        while low < high:
            mid = (low + high) // 2
            if checkPath(mid):
                high = mid
            else:
                low = mid+1
        
        
        return low
        