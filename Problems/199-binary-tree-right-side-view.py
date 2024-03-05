// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol = {}
    def solve(self, node, level):
        if node:
            if level not in self.sol:
                self.sol[level] = [node.val]
            else:
                self.sol[level].append(node.val)
            self.solve(node.left, level+1)
            self.solve(node.right, level+1)
            
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.solve(root, 0)
        res = [self.sol[i][-1] for i in range(len(self.sol))]
        return res
        
        