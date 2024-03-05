// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        factors = set()
        for n in nums:
            for p in prime_list:
                if n % p == 0:
                    factors.add(p)
                    while n % p == 0:
                        n = n/p
            if n != 1:
                factors.add(n)
        
        return len(factors)