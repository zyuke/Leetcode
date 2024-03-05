// https://leetcode.com/problems/sort-array-by-parity-ii

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [0 for i in range(len(A))]
        odd = 1; even = 0
        for i in A:
            if i % 2 == 0:
                res[even] = i
                even += 2
            else:
                res[odd] = i
                odd += 2
        return res