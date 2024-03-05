// https://leetcode.com/problems/out-of-boundary-paths

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = {}
        def search(row, col, move):
            if (row, col, move) in dp:
                return dp[(row, col, move)]
            if move < 0:
                return 0
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            l = search(row, col-1, move-1)
            r = search(row, col+1, move-1)
            u = search(row-1, col, move-1)
            d = search(row+1, col, move-1)
            dp[(row, col, move)] = (l+r+u+d) % 1000000007
            return dp[(row, col, move)]
        
        res = search(startRow, startColumn, maxMove)
        return res
            