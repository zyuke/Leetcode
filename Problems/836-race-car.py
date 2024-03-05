// https://leetcode.com/problems/race-car

class Solution:
    def racecar(self, target: int) -> int:
        dp = {0:0}
        def search(i):
            if i in dp:
                return dp[i]
            n = i.bit_length()
            if 2**n-1 == i:
                dp[i] = n
            else:
                dp[i] = search(2**n-1-i)+n+1
                for m in range(n-1):
                    dp[i] = min(dp[i],search(i-2**(n-1)+2**m)+n+m+1)
            
            return dp[i]
        
        return search(target)