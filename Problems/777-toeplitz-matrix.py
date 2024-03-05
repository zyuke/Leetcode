// https://leetcode.com/problems/toeplitz-matrix

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        for j in range(m):
            x = 0; y = j
            v = matrix[x][y]
            while 0<=x<=n-1 and 0<=y<=m-1:
                if matrix[x][y] != v:
                    return False
                x += 1
                y += 1
        
        for i in range(n):
            x = i; y = 0
            v = matrix[x][y]
            while 0<=x<=n-1 and 0<=y<=m-1:
                if matrix[x][y] != v:
                    return False
                x += 1
                y += 1
            
        return True