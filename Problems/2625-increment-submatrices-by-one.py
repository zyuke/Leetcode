# https://leetcode.com/problems/increment-submatrices-by-one

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        aux = [[0]*n for _ in range(n)]
        for (x1,y1,x2,y2) in queries:
            aux[x1][y1] += 1
            if x2 +1 < n :
                aux[x2+1][y1] -= 1
            if x2+1<n and y2+1<n:
                aux[x2+1][y2+1] +=1
            if y2+1<n:
                aux[x1][y2+1]-=1
        
        # print(aux)
        
        for i in range(n):
            for j in range(1,n):
                aux[i][j] += aux[i][j-1]
        for i in range(n):
            for j in range(1,n):
                aux[j][i] += aux[j-1][i]
                
        return aux