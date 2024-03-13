# https://leetcode.com/problems/find-original-array-from-doubled-array

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count = Counter(changed)
        res = []
        
        for n in changed:
            if count[n] == 0: continue
            double = int(2*n)
            count[n] -= 1
            if count[double] > 0:
                res.append(n)
                count[double] -= 1
            else:
                return []
        return res