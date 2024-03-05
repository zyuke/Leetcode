// https://leetcode.com/problems/reduce-array-size-to-the-half

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ct = {}
        for i in arr:
            if i in ct:
                ct[i] += 1
            else:
                ct[i] = 1
        
        temp = [ct[k] for k in ct]
        sort_ct = sorted(temp, reverse = True)
        cutoff = len(arr) // 2
        
        res = 0
        amt = 0
        for i in sort_ct:
            amt += i
            res += 1
            if amt >= cutoff:
                return res