// https://leetcode.com/problems/student-attendance-record-ii

class Solution:
    def checkRecord(self, n: int) -> int:
        a = [1,3,8,19]
        if n < 4:
            return a[n]
        
        M = 1000000007
        f = [0] * (n+1)
        f[0] = 1; f[1] = 2; f[2] = 4; f[3] = 7
        
        for i in range(4, n+1):
            f[i] = (f[i-1] + f[i-2] + f[i-3]) % M
        
        # print(f)
        res = 0
        for i in range(1, n+1):
            res = (res + f[i-1]*f[n-i]) % M
        
        return (f[n] + res) % M
        