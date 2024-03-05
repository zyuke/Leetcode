// https://leetcode.com/problems/check-if-it-is-a-good-array

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        gcd = nums[0]
        def GCD(a, b):
            while b != 0:
                t = b
                b = a % b
                a = t
            return a
        
        for n in nums:
            gcd = GCD(gcd, n)
            if gcd == 1:
                return True
        return False
