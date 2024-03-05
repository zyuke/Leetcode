// https://leetcode.com/problems/minimum-penalty-for-a-shop

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curEmpty = 0
        futureCustomer = sum([1 for c in customers if c == 'Y'])
        minHour = -1
        minPenalty = float('inf')
        for i in range(len(customers)):
            curPenalty = futureCustomer + curEmpty
            if customers[i] == 'Y':
                futureCustomer -= 1
            else:
                curEmpty += 1
            if curPenalty < minPenalty:
                minPenalty = curPenalty
                minHour = i
        if curEmpty < minPenalty:
            return len(customers)
        return minHour