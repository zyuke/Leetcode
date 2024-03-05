// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left, right = 0, 0
        for c in S:
            if right == 0 and c ==')':
                left += 1
            elif c == '(':
                right += 1
            elif c == ')':
                right -= 1
        return left + right