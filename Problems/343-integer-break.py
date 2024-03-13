# https://leetcode.com/problems/integer-break

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 3:
            return 2
        if n == 2:
            return 1
        res = 1
        N = n
        while N != 0:
            if N >= 3:
                res *= 3
                N -= 3
            if N == 1:
                res /= 3
                N += 3
                res *= 2
                N -= 2
            if N == 2:
                N -= 2
                res *= 2
                
        
        return res