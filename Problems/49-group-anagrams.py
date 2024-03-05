// https://leetcode.com/problems/group-anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        for s in strs:
            t = ''.join(sorted(s))
            try:
                group[t].append(s)
            except:
                group[t] = [s]
                
        return [group[k] for k in group]
        
        