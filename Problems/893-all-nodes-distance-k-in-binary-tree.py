# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        G = {}
        res = []
        visited = set()
        visited.add(target.val)
        self.initialize(root, G)
        self.build_graph(root, G)
        self.bfs(target.val, K, G, visited, res)
        
        return res
        
    def initialize(self, root, G):
        if root:
            G[root.val] = []
            self.initialize(root.left, G)
            self.initialize(root.right, G)
        
    def build_graph(self, root, G):
        if root:
            if root.left:
                G[root.val].append(root.left.val)
                G[root.left.val].append(root.val)
                self.build_graph(root.left, G)
            if root.right:
                G[root.val].append(root.right.val)
                G[root.right.val].append(root.val)
                self.build_graph(root.right, G)
                
    def bfs(self, cur, K, G, visited, res):
        if K == 0:
            res.append(cur)
        else:
            for next_val in G[cur]:
                if next_val not in visited:
                    visited.add(next_val)
                    self.bfs(next_val, K-1, G, visited, res)
                    