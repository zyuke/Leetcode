class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        def check_palindrome(i, j, dp):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == j:
                dp[(i, j)] = True
                return True
            if i + 1 == j:
                dp[(i, j)] = (s[i] == s[j])
                return dp[(i, j)]

            if s[i] == s[j] and check_palindrome(i+1, j-1, dp):
                dp[(i, j)] = True
            else:
                dp[(i, j)] = False
            return dp[(i, j)] 

        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if check_palindrome(i, j, dp):
                    res += 1

        return res
        
