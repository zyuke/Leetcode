// https://leetcode.com/problems/single-number-iii

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for i in nums:
            xor = xor^i
            
        mask = 1
        while mask & xor == 0:
            mask = mask << 1
        
        a = 0
        b = 0
        
        for i in nums:
            if i & mask:
                a = a^i
            else:
                b = b^i
                
        return [a,b]