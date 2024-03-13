# https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        res = 0
        
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                cur_height = heights[stack.pop()]
                cur_w = i-stack[-1]-1
                res = max(res, cur_height*cur_w)
            stack.append(i)
        
        while stack[-1] != -1:
            cur_height = heights[stack.pop()]
            cur_w = len(heights) - stack[-1] -1
            res = max(res, cur_height*cur_w)
        
        return res