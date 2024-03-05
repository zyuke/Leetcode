// https://leetcode.com/problems/maximum-average-subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.maxAve = 0
        self.dfs(root)
        return self.maxAve
        
    def dfs(self, root):
        if not root:
            return 0, 0
        if root:
            left_ave, left_size = self.dfs(root.left)
            right_ave, right_size = self.dfs(root.right)
            cur_ave = (left_ave*left_size + right_ave*right_size + root.val) / (left_size + right_size + 1)
            cur_size = left_size + right_size + 1

            if cur_ave > self.maxAve:
                self.maxAve = cur_ave

            return cur_ave, cur_size