# https://leetcode.com/problems/jewels-and-stones

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if S[j] == J[i]:
                    count += 1
        return count