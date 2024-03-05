// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        median  = len(nums)/2
        new_node = TreeNode(nums[median])

        new_node.left = self.sortedArrayToBST(nums[:median])
        new_node.right = self.sortedArrayToBST(nums[median+1:])
        
        return new_node