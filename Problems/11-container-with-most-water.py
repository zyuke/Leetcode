# https://leetcode.com/problems/container-with-most-water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = i = 0
        j = len(height)-1
        
        while j>i:
            max_area = max(max_area, (j-i)*min(height[i], height[j]))
            if height[i] > height[j]:
                j = j-1
            else:
                i = i+1
        
        return max_area