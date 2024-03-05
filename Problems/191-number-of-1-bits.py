// https://leetcode.com/problems/number-of-1-bits

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = "{0:b}".format(n)
        return s.count('1')