# https://leetcode.com/problems/insert-into-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        self.helper(root, val)
        return root
        
        
    def helper(self, root, val):
        if root.val < val and root.right:
            self.helper(root.right, val)
        elif root.val < val and not root.right:
            root.right = TreeNode(val)
        elif root.val > val and root.left:
            self.helper(root.left, val)
        elif root.val > val and  not root.left:
            root.left = TreeNode(val)
        