# https://leetcode.com/problems/k-concatenation-maximum-sum

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        M = 1000000007
        curMax = 0
        curSum = 0
        for n in arr:
            curSum += n
            if curSum > 0:
                curMax = max(curMax, curSum)
            else:
                curSum = 0
        res = [curMax]

        s = sum(arr)
        if s > 0:
            t = s*k
            res.append(t)

        if k > 1:
            maxPreSum = 0
            maxSufSum = s
            curPreSum = 0
            curSufSum = s
            for n in arr:
                curPreSum += n
                curSufSum -= n
                maxPreSum = max(maxPreSum, curPreSum)
                maxSufSum = max(maxSufSum, curSufSum)
            if s > 0:
                total = maxPreSum + maxSufSum + (k-2)*s
            if s <= 0:
                total = maxPreSum + maxSufSum
            res.append(total)
       
        return max(res) % M