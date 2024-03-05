// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        traversed = dict()
        queue = [node]
        traversed[node] = Node(node.val, [])
        
        while queue:
            next_node = queue.pop(0)
            for neighbor in next_node.neighbors:
                if neighbor not in traversed:
                    queue.append(neighbor)
                    copy_neighbor = Node(neighbor.val, [])
                    traversed[neighbor] = copy_neighbor
            
                traversed[next_node].neighbors.append(traversed[neighbor])
                
        return traversed[node]
            
                
                
        
        