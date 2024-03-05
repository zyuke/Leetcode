// https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        def traverse(node):
            if node:
                traverse(node.left)
                nodes.append(node)
                traverse(node.right)
        traverse(root)
        print(nodes)
        wrong_node_1 = None
        wrong_node_2 = None
        for i in range(len(nodes)-1):
            if nodes[i].val > nodes[i+1].val:
                wrong_node_1 = nodes[i]
                break
        for i in range(len(nodes)-1, 0, -1):
            if nodes[i].val < nodes[i-1].val:
                wrong_node_2 = nodes[i]
                break
        
        wrong_node_1.val, wrong_node_2.val = wrong_node_2.val, wrong_node_1.val