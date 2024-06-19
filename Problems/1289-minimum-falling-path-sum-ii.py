class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if N == 1:
            return grid[0][0]
        
        def find_two_min(L):
            i0, x0, i1, x1 = -1, float('inf'), -1, float('inf')
            for i, x in enumerate(L):
                if x < x0:
                    i1, x1 = i0, x0
                    i0, x0 = i, x
                else:
                    if x < x1:
                        i1, x1 = i, x
            return (i0, x0, i1, x1)

        min_val, min_col = 0, -1
        second_min_val, second_min_col = 0, -1

        for row in range(N):
            col_vals = []
            for col in range(N):
                if col != min_col:
                    col_vals.append(grid[row][col] + min_val)
                else:
                    col_vals.append(grid[row][col] + second_min_val)
            min_col, min_val, second_min_col, second_min_val = find_two_min(col_vals)

        return min_val
