# https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.val  = root.val
        self.res = True
        self.search(root)
        return self.res
        
    def search(self, root):
        if not root:
            return
        if root.val != self.val:
            self.res = False
            return
        
        self.search(root.left)
        self.search(root.right)