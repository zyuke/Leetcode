// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
      
        if root is None:
            return ""

        dq = collections.deque()
        dq.append((root, ""))
        start_found = False
        dest_found = False
        start_path = ""
        dest_path = ""
        while len(dq) > 0 and not (start_found and dest_found):
            node, path = dq.popleft()
            if node.val == startValue:
                start_found = True
                start_path = path
            elif node.val == destValue:
                dest_found = True
                dest_path = path
            if node.left is not None:
                dq.append((node.left, path + "L"))
            if node.right is not None:
                dq.append((node.right, path + "R"))
        i = 0
        while len(start_path) > i and len(dest_path) > i and start_path[i] == dest_path[i]:
            i += 1
        return (len(start_path) - i) * 'U' + dest_path[i:]
    
        
        