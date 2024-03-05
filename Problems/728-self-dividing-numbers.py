// https://leetcode.com/problems/self-dividing-numbers

class Solution(object):
    def is_self_dividing(self,x):
        s = str(x)
        for d in s:
            if d=="0" or x%int(d)!=0:
                return False
        return True
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            if self.is_self_dividing(i):
                result.append(i)
        return result