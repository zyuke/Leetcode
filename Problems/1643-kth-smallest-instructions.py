from math import factorial

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        M, N = destination[0], destination[1]

        def helper(M, N, k):
            if M == 0: 
                return 'H'*N
            if N == 0:
                return 'V'*M
            d = factorial(N+M-1) // (factorial(N-1)*factorial(M))
            if k <= d:
                return 'H' + helper(M, N-1, k)
            else:
                return 'V' + helper(M-1, N, k-d)

        return helper(M, N, k)
