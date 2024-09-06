# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def traverse(node, vals):
            if node.left:
                traverse(node.left, vals)
            if node:
                vals.append(node.val)
            if node.right:
                traverse(node.right, vals)

        vals = []
        traverse(root, vals)

        def build_tree(vals, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(vals[mid])
            root.left = build_tree(vals, left, mid-1)
            root.right = build_tree(vals, mid+1, right)
            return root

        return build_tree(vals, 0, len(vals)-1)

