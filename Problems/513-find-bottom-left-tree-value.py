// https://leetcode.com/problems/find-bottom-left-tree-value

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue=[root]; ans=0
        while any(queue):
            ans=queue[0].val
            queue=[leaf for node in queue for leaf in (node.left,node.right) if leaf]
        return ans