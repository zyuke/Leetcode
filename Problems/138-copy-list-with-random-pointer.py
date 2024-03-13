# https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        self.visited = {}
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        
        new_node = Node(head.val, None, None)
        self.visited[head] = new_node
        
        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)
        
        return new_node