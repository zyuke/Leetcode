// https://leetcode.com/problems/amount-of-new-area-painted-each-day

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        res = []
        skip = dict()
        for start, end in paint:
            area = 0
            while start < end:
                if start in skip:
                    start = skip[start]
                else:
                    area += 1
                    skip[start] = end
                    start += 1
            
            res.append(area)
        return res