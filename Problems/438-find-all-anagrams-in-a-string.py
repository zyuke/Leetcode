// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        res = []
        pcounter = Counter(p)
        scounter = Counter(s[:len(p)-1])
        
        for i in range(len(p)-1, len(s)):
            scounter[s[i]] += 1
            if scounter == pcounter:
                res.append(i-len(p)+1)
            scounter[s[i-len(p)+1]] -= 1
            if scounter[s[i-len(p)+1]] == 0:
                del scounter[s[i-len(p)+1]]
                
        return res
        