class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if grid[-1][-1] == -1:
            return 0

        self.grid = grid
        self.dp = {}

        return max(0, self.solve(0, 0, 0, 0))

    def solve(self, x1, y1, x2, y2):
        if (x1, y1, x2, y2) in self.dp:
            return self.dp[(x1, y1, x2, y2)]

        N = len(self.grid)
        if x1 == N or y1 == N or x2 == N or y2 == N:
            return -1
        if self.grid[x1][y1] == -1 or self.grid[x2][y2] == -1:
            return -1
        if x1 == y1 == x2 == y2 == N-1:
            return self.grid[-1][-1]

        dd = self.solve(x1+1, y1, x2+1, y2)
        dr = self.solve(x1+1, y1, x2, y2+1)
        rd = self.solve(x1, y1+1, x2+1, y2)
        rr = self.solve(x1, y1+1, x2, y2+1)
        maxComb = max(dd, dr, rd, rr)

        if maxComb == -1:
            res = -1
        else:
            if x1 == x2 and y1 == y2:
                res = maxComb + self.grid[x1][y1]
            else:
                res = maxComb + self.grid[x1][y1] + self.grid[x2][y2]

        self.dp[(x1, y1, x2, y2)] = res
        return res
