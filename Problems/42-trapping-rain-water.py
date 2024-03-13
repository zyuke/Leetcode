# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        res = 0
        
        cur_max = 0
        for i in range(len(height)):
            cur_max = max(cur_max, height[i])
            left_max.append(cur_max)
        
        cur_max = 0
        for i in range(len(height)-1, -1, -1):
            cur_max = max(cur_max, height[i])
            right_max.append(cur_max)
        right_max = right_max[::-1]
        
        for i in range(len(height)):
            res += min(left_max[i], right_max[i]) - height[i]
            
        return res