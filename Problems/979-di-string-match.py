# https://leetcode.com/problems/di-string-match

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        N = len(S)
        numbers = range(N+1)
        for s in S:
            if s == 'I':
                res.append(numbers[0])
                numbers.pop(0)
            if s == 'D':
                res.append(numbers[-1])
                numbers.pop(-1)
        res.append(numbers[0])
        return res
            