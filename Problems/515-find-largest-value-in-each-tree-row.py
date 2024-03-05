// https://leetcode.com/problems/find-largest-value-in-each-tree-row

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rows = dict()
        def helper(root, depth):
            if root:
                if depth in rows:
                    rows[depth].append(root.val)
                else:
                    rows[depth] = [root.val]
                    
                helper(root.left, depth+1)
                helper(root.right, depth+1)
            
        helper(root, 0)
        
        res = []
        for key in rows:
            res.append(max(rows[key]))
            
        return res