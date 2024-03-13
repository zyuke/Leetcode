# https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        def get(window):
            cur_max = -1*0xfffff; idx = 0
            for i in range(k):
                if window[i] >= cur_max:
                    cur_max = window[i]
                    idx = i
            return cur_max, idx
        
        
        window = nums[:k]
        m, x = get(window)
        res = [m]
        
        for i in range(k, len(nums)):
            window.pop(0)
            window.append(nums[i])
            x -= 1
            
            if x < 0:
                m, x = get(window)
                
            elif nums[i] >= m:
                m = nums[i]
                x = k-1
            
                
            res.append(m)
            
        return res