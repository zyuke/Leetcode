# https://leetcode.com/problems/binary-tree-vertical-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        level = defaultdict(list)
        queue = [(root, 0)]
        
        for node, i in queue:
            if node:
                level[i].append(node.val)
                queue += [(node.left, i-1), (node.right, i+1)]
        
        res = []
        if level:
            idx = min(level.keys())
            while idx in level:
                res.append(level[idx])
                idx += 1
        
        return res