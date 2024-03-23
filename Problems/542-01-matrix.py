class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        def valid(x, y):
            return 0 <= x < m and 0 <= y < n

        from collections import deque
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        while queue:
            x, y = queue.popleft()
            for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x+dx, y+dy
                if valid(new_x, new_y) and mat[new_x][new_y] == -1:
                    mat[new_x][new_y] = mat[x][y] + 1
                    queue.append((new_x, new_y))

        return mat            
