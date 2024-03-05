// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
            
        def to_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            
            preorder_index += 1
            
            root.left = to_tree(left, inorder_map[root_val]-1)
            root.right = to_tree(inorder_map[root_val]+1, right)
            
            return root
        
        preorder_index = 0
        return to_tree(0, len(preorder)-1)