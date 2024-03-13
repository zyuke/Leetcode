# https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        res = [0]
        def counter(root, res):
            if root:
                res[0] += 1
                counter(root.left, res)
                counter(root.right, res)
        counter(root, res)
        return res[0]
        