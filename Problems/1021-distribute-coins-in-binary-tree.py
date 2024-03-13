# https://leetcode.com/problems/distribute-coins-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root):
            if root == None:
                return 0
            L = dfs(root.left)
            R = dfs(root.right)
            self.res += abs(L) + abs(R)
            return root.val+L+R-1
        
        dfs(root)
        return self.res