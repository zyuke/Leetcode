// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sol = 0
        def depth(root):
            if not root:
                return 0
            else:
                left, right = depth(root.left), depth(root.right)
                self.sol = max(self.sol, left+right)
                return max(left,right)+1
            
        depth(root)
        return self.sol
