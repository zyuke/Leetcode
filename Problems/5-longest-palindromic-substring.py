// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        P = [[False] * n for _ in range(n)]
        cur_max_len = 0
        res = s[0]
        
        for i in range(n):
            P[i][i] = True
            
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if i + 1 == j or P[i+1][j-1]:
                        P[i][j] = True
                        if j - i + 1 > cur_max_len:
                            cur_max_len = j - i + 1
                            res = s[i:j+1]
        
        return res