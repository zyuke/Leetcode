class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(1, N):
                matrix[i][j] += matrix[i][j-1]

        res = 0
        for c1 in range(N):
            for c2 in range(c1, N):
                prefix_sum_ct = {0: 1}
                tot = 0
                for r in range(M):
                    tot += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                    res += prefix_sum_ct.get(tot - target, 0)
                    prefix_sum_ct[tot] = prefix_sum_ct.get(tot, 0) + 1

        return res
