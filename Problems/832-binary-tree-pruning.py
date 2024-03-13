# https://leetcode.com/problems/binary-tree-pruning

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def zero(root):
            if not root:
                return 0
            return root.val+zero(root.left)+zero(root.right)
            
        def prune(root):
            if root:
                if zero(root.left) == 0:
                    root.left = None
                if zero(root.right) == 0:
                    root.right = None
                prune(root.left)
                prune(root.right)
                    
        prune(root)
        return root