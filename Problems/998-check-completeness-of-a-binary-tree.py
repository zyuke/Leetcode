// https://leetcode.com/problems/check-completeness-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        level_map = dict()
        def bfs(node, level):
            if not node:
                if level in level_map:
                    level_map[level].append(-1)
                else:
                    level_map[level] = [-1]
            else:
                if level in level_map:
                    level_map[level].append(node.val)
                else:
                    level_map[level] = [node.val]
                bfs(node.left, level+1)
                bfs(node.right, level+1)
        
        bfs(root, 0)
        is_complete = True
        max_level = max(level_map)
        # print(level_map)
        del level_map[max_level]
        max_level = max(level_map)
        print(level_map)
        for level in level_map:
            if level != max_level:
                if sum([1 for x in level_map[level] if x != -1]) != 2**level:
                       return False
            else:
                seen_null = False
                for i in range(len(level_map[level])):
                    if level_map[level][i] == -1:
                        seen_null = True
                    else:
                        if seen_null:
                            return False
        return True