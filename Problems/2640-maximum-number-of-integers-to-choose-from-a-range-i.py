# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        cur_sum = 0
        ct = 0
        for i in range(1, n+1):
            if not i in ban:
                cur_sum += i
                if cur_sum > maxSum:
                    return ct
                ct += 1
        return ct