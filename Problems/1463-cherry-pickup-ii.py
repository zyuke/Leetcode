from collections import defaultdict

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = defaultdict(lambda: 0)
        R, C = len(grid), len(grid[0])
        for row in reversed(range(R)):
            for c1 in range(C):
                for c2 in range(C):
                    if c1 == c2:
                        cur_base = grid[row][c1]
                    else:
                        cur_base = grid[row][c1] + grid[row][c2]
                    prev_max = 0
                    for d_c1 in [-1, 0, 1]:
                        for d_c2 in [-1, 0, 1]:
                            new_c1 = c1 + d_c1
                            new_c2 = c2 + d_c2
                            prev_max = max(prev_max, dp[(row+1, new_c1, new_c2)])
                    dp[(row, c1, c2)] = cur_base + prev_max

        return dp[(0, 0, C-1)]
