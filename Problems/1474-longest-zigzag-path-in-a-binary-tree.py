# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        dp_left = {}
        dp_right = {}
        
        def search(node, direction):
            if node:
                if node.left:
                    if node.left not in dp_left:
                        dp_left[node.left] = search(node.left, 0)
                    if node.left not in dp_right:
                        dp_right[node.left] = search(node.left, 1)
                        
                if node.right:
                    if node.right not in dp_left:
                        dp_left[node.right] = search(node.right, 0)
                    if node.right not in dp_right:
                        dp_right[node.right] = search(node.right, 1)
                    
                if direction == 0:
                    if node.left:
                        dp_left[node] = dp_right[node.left] + 1
                    else:
                        dp_left[node] = 0
                    return dp_left[node]
                
                if direction == 1:
                    if node.right:
                        dp_right[node] = dp_left[node.right] + 1
                    else:
                        dp_right[node] = 0
                    return dp_right[node]
        
        res = 0
        search(root, 0)
        search(root, 1)
        
        for k in dp_left:
            res = max(res, dp_left[k])
        for k in dp_right:
            res = max(res, dp_right[k])
        return res

                    
                    