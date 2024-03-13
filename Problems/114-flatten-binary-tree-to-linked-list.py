# https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.node_order = []
        def traverse(root):
            if root:
                self.node_order.append(root)
                traverse(root.left)
                traverse(root.right)
        
        traverse(root)
        for i in range(len(self.node_order)-1):
            self.node_order[i].left = None
            self.node_order[i].right = self.node_order[i+1]
        