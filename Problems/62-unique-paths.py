// https://leetcode.com/problems/unique-paths

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        from math import factorial
        return math.factorial(m+n-2)/(math.factorial(n-1))/math.factorial(m-1)