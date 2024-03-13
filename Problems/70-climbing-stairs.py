# https://leetcode.com/problems/climbing-stairs


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((pow((1+math.sqrt(5))/2,n+1)-pow((1-math.sqrt(5))/2,n+1))/math.sqrt(5))
        