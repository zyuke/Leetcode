# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = []
        for i in range(len(prices)-1):
            diff.append(prices[i+1]-prices[i])
        
        result = 0
        for x in diff:
            if x > 0:
                result += x
                
        return result