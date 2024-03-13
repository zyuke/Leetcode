# https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            try:
                freq[c] += 1
            except:
                freq[c] = 1
        
        S = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        res = ''
        for t in S:
            res += t[0]*t[1]
            
        return res