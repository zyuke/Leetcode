// https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.helper(root, [], 0, sum, res)
        return res
        
    def helper(self, root, path, s, target, res):
        if root:
            new_s = s + root.val
            new_path = path + [root.val]
            
            if new_s == target and root.left == None and root.right == None:
                res.append(new_path)
            
            self.helper(root.left, new_path, new_s, target, res)
            self.helper(root.right, new_path, new_s, target, res)
            

                    

                    