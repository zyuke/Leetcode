// https://leetcode.com/problems/most-profit-assigning-work

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        d2p = [(difficulty[i], profit[i]) for i in range(len(profit))]
        s_d2p = sorted(d2p)
        res = best = i = 0
        
        for skill in sorted(worker):
            while i < len(worker) and skill >= s_d2p[i][0]:
                best = max(best, s_d2p[i][1])
                i += 1

            res += best
            
        return res