# https://leetcode.com/problems/number-complement

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        t = 1
        while t <= num:
            t = t*2
        
        return t - num - 1