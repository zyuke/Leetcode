// https://leetcode.com/problems/maximum-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        maxval = max(nums)
        max_index = nums.index(maxval)
        
        res = TreeNode(maxval)
        res.left = self.constructMaximumBinaryTree(nums[:max_index])
        res.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        
        return res