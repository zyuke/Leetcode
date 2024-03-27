# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1*float('inf') 
        def max_from_node(node):
            if not node:
                return 0
            left = max(0, max_from_node(node.left))
            right = max(0, max_from_node(node.right))
            self.res = max(self.res, left + right + node.val)
            return max(0, left, right) + node.val

        max_from_node(root)
        return self.res
