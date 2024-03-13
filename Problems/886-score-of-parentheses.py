# https://leetcode.com/problems/score-of-parentheses

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        l_count = 0
        res = 0
        N = len(S)
        
        for i in range(N-1):
            if S[i] == '(':
                if S[i+1] == ')':
                    res += 1 << l_count
                l_count += 1
            else:
                l_count -= 1
        
        return res
                    