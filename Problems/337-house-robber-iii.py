# https://leetcode.com/problems/house-robber-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def search(node):
            if not node:
                return (0, 0)
            
            left, right = search(node.left), search(node.right)
            now = node.val + left[1] + right[1]
            later = max(left) + max(right)
            
            return (now, later)
        
        return max(search(root))