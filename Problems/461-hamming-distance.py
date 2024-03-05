// https://leetcode.com/problems/hamming-distance

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        xor = x^y
        b_xor = "{0:b}".format(xor)
        l_xor = list(b_xor)
        return l_xor.count('1')