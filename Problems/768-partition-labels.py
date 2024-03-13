# https://leetcode.com/problems/partition-labels

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(S)}
        start = end = 0
        res = []
        
        for i, c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
                
        return res