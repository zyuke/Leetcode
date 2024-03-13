# https://leetcode.com/problems/counting-bits

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        from math import log
        
        res = [0]
        offset = 1
        
        for i in range(1, num+1):
            if offset*2 == i:
                offset = 2*offset
            res.append(1 + res[i-offset])
        
        return res
        
        