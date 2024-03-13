# https://leetcode.com/problems/maximum-split-of-positive-even-integers

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        cur_sum = 0
        cur_num = 2
        res = []
        while True:
            cur_sum += cur_num
            if cur_sum < finalSum:
                res.append(cur_num)
                cur_num += 2
            if cur_sum == finalSum:
                res.append(cur_num)
                break
            if cur_sum > finalSum:
                diff = cur_sum - finalSum
                last = res.pop()
                res.append(last+cur_num-diff)
                break
            
        
        return res