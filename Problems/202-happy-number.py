// https://leetcode.com/problems/happy-number

def sum_digits(n):
    s = 0
    while n:
        s += (n % 10)**2
        n //= 10
    return s

class Solution(object):
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_list = []
        temp = n
        sum_temp = sum_digits(temp)
        while sum_temp not in sum_list:
            if sum_temp == 1:
                return True
            sum_list.append(sum_temp)
            temp = sum_temp
            sum_temp = sum_digits(temp)
        return False