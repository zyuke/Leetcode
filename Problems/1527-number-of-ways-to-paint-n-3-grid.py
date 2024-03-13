# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid

class Solution:
    def numOfWays(self, n: int) -> int:
        M = 1000000007
        T2 = 6
        T3 = 6
        for _ in range(1, n):
            next_T3 = (2*T2+2*T3) % M
            next_T2 = (3*T2+2*T3) % M
            T2 = next_T2
            T3 = next_T3
        return (T2+T3) % M