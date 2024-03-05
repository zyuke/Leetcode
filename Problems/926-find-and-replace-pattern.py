// https://leetcode.com/problems/find-and-replace-pattern

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def helper(w):
            count = 0
            dict_w = dict()
            res = []
            for c in w:
                if c in dict_w:
                    res.append(dict_w[c])
                else:
                    dict_w[c] = count
                    res.append(count)
                    count += 1
            return res
        
        result = []
        pat_id = helper(pattern)
        for w in words:
            if helper(w) == pat_id:
                result.append(w)
        
        return result