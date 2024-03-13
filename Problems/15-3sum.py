# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_set = set(nums)
        if len(nums) > 2 and len(num_set) == 1 and nums[0] == 0:
            return [[0,0,0]]
        
        def two_sum(nums, target):
            res = []
            ct = set()
            for n in nums:
                if n in ct:
                    res.append([-target, target - n, n])
                ct.add(target - n)
                
            return res
        
        res = []
        for i in range(len(nums) - 1):         
            res += two_sum(nums[i+1:], -nums[i])
        
        res_set = set()
        for tri in res:
            res_set.add(tuple(sorted(tri)))
        
        ret = [t for t in res_set]
        
        return ret