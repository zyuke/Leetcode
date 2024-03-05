// https://leetcode.com/problems/valid-anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_l = list(s)
        t_l = list(t)
        
        return sorted(s_l) == sorted(t_l)