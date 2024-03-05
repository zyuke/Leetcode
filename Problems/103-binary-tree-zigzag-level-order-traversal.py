// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        d = dict()
        def get_level(node, level = 0):
            if node:
                if level not in d:
                    d[level] = [node.val]
                else:
                    d[level].append(node.val)
                
                get_level(node.left, level + 1)
                get_level(node.right, level + 1)
        
        get_level(root, 0)
        res = []
        for i in d:
            if i % 2 == 1:
                res.append(d[i][::-1])
            else:
                res.append(d[i])
        return res
        