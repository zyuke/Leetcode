# https://leetcode.com/problems/pascals-triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        if numRows >= 1:
            ans.append([1])
        if numRows >= 2:
            ans.append([1, 1])
        for row in range(2, numRows):
            res = [1, 1]
            for i in range(1, row):
                res.insert(i, sum(ans[row - 1][i-1:i+1]))
            ans.append(res)
        return ans