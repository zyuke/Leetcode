// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = dict()
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            if s[i] in seen and start <= seen[s[i]]:
                start = seen[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            
            seen[s[i]] = i
            
        return max_len
                
                