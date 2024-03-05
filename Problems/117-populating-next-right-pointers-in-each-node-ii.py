// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level = dict()
        def search(node, depth):
            if node:
                if depth in level:
                    level[depth].append(node)
                else:
                    level[depth] = [node]
                search(node.left, depth+1)
                search(node.right, depth+1)
                
        search(root, 0)
        
        for l in level:
            level[l].append(None)
            for i in range(len(level[l])-1):
                level[l][i].next = level[l][i+1]
                
        return root