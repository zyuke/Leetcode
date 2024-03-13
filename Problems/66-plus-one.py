# https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        number = 0
        for i in range(n):
            number += 10**(n-1-i)*digits[i]
        return map(int, str(number+1))