# https://leetcode.com/problems/delete-node-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        elif root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            temp = root.right
            temp_val = temp.val
            while temp.left:
                temp = temp.left
                temp_val = temp.val
            root.val = temp_val
            root.right = self.deleteNode(root.right, temp_val)
        
        return root