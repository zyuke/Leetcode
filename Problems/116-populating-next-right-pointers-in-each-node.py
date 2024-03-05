// https://leetcode.com/problems/populating-next-right-pointers-in-each-node

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        def get_level(root, level):
            if not root:
                return []
            if level == 0:
                return [root]
            if level > 0:
                return get_level(root.left, level-1) + get_level(root.right, level-1)
            
        L = 0; temp = root
        while temp:
            L += 1
            temp = temp.left
        
        for i in range(L):
            l_nodes = get_level(root, i)
            l_nodes.append(None)
            for x in range(len(l_nodes) - 1):
                l_nodes[x].next = l_nodes[x+1]
        
        return root
    