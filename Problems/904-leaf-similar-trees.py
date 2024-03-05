// https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        l1, l2 = [], []
        def getl(root, l):
            if root:
                getl(root.left, l)
                if root.left == None and root.right == None:
                    l.append(root.val)
                getl(root.right, l)
            
        getl(root1, l1)
        getl(root2, l2)
        
        return l1 == l2