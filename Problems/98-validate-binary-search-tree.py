# https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(root, lower = float('-inf'), upper = float('inf')):
            if not root:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
            
            if not validate(root.left, lower, root.val):
                return False
            
            if not validate(root.right, root.val, upper):
                return False
            
            return True
        
        return validate(root)