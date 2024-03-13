# https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.level_map = {}
        def search(node, level):
            if node:
                try:
                    self.level_map[level].append(node.val)
                except:
                    self.level_map[level] = [node.val]
                search(node.left, level+1)
                search(node.right, level+1)
        
        search(root, 0)
        res = [self.level_map[k] for k in self.level_map]
        return res