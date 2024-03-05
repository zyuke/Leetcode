// https://leetcode.com/problems/factorial-trailing-zeroes

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum([n/5**(i+1) for i in range(int(__import__('math').log(max(1,n),5)))])