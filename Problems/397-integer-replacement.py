# https://leetcode.com/problems/integer-replacement

class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {1:0}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n in memo:
            return memo[n]
        else:
            if n % 2 == 1:
                memo[n] = 1 + min(self.helper(n+1, memo), self.helper(n-1, memo))
                return memo[n]
            else:
                memo[n] = 1 + self.helper(n/2, memo)
                return memo[n]
            
            