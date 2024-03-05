// https://leetcode.com/problems/range-sum-query-2d-immutable

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.partial_sum = {}
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            self.partial_sum[(i,-1)] = 0
        for j in range(n):
            self.partial_sum[(-1,j)] = 0
        self.partial_sum[(-1,-1)] = 0
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += matrix[i][j]
                self.partial_sum[(i,j)] = row_sum + self.partial_sum[(i-1,j)]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.partial_sum[(row2, col2)] - self.partial_sum[(row1-1, col2)] - self.partial_sum[(row2, col1-1)] + self.partial_sum[(row1-1, col1-1)]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)