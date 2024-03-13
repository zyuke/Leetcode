# https://leetcode.com/problems/flipping-an-image

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        def flip(L):
            result = []
            for i in L:
                result.append((i+1)%2)
            return result
        
        result = []
        for L in A:
            result.append(flip(L[::-1]))
        return result