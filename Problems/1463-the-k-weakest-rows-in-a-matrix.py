# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        D = []
        for i in range(len(mat)):
            n = int(''.join([str(x) for x in mat[i]]))
            D.append((i, n))
        D.sort(key=lambda x: (x[1], x[0]))
        return [D[i][0] for i in range(k)]
        