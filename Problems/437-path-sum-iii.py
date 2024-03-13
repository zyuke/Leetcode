# https://leetcode.com/problems/path-sum-iii

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.num_path = 0
        self.dfs(root, sum)
        
        return self.num_path
        
    def dfs(self, node, sum):
        if node:
            self.test(node, sum)
            self.dfs(node.left, sum)
            self.dfs(node.right, sum)
                
    def test(self, node, sum):
        if node:
            if node.val == sum:
                self.num_path += 1
            self.test(node.left, sum - node.val)
            self.test(node.right, sum - node.val)
                
        
        