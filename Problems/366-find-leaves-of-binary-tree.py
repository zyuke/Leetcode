# https://leetcode.com/problems/find-leaves-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        height2nodeval = dict()
        def dfs(node):
            if not node:
                return -1
            else:
                lv = dfs(node.left)
                rv = dfs(node.right)
                height = max(lv,rv) + 1
                if height in height2nodeval:
                    height2nodeval[height].append(node.val)
                else:
                    height2nodeval[height] = [node.val]
                return height
            
        dfs(root)
        
        i = 0
        res = []
        while i in height2nodeval:
            res.append(height2nodeval[i])
            i += 1
        return res