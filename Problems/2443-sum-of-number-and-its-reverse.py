# https://leetcode.com/problems/sum-of-number-and-its-reverse/

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def reverse(num):
            s_num = str(num)
            digits = [int(c) for c in s_num]
            pow = 1
            ret = 0
            N = len(digits)
            for i in range(N):
                ret += digits[i]*pow
                pow = pow*10
            return ret
        
        for i in range(num+1):
            if i + reverse(i) == num:
                return True
        return False 
