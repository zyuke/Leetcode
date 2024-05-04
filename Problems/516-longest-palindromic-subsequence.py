class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        n = len(s)
        for i in range(n):
            dp[(i, i)] = 1

        def helper(i, j):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == s[j]:
                temp = helper(i+1, j-1) + 2
                dp[(i, j)] = temp
                return temp
            else:
                temp = max(helper(i+1, j), helper(i, j-1))
                dp[(i, j)] = temp
                return temp

        return helper(0, n-1)
        
