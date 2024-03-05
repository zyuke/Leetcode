// https://leetcode.com/problems/find-and-replace-in-string

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ops = [(indices[i],sources[i],targets[i]) for i in range(len(indices))]
        ops.sort()
        
        start = 0
        res = ""
        for idx, source, target in ops:
            if s[idx:idx+len(source)] == source:
                res += s[start:idx]
                res += target
                start = idx+len(source)
        res += s[start:]
        return res
                
            