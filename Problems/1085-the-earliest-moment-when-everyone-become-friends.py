# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        group = UnionFind(n)
        group_num = n
        for t, x, y in logs:
            if group.union(x, y):
                group_num -= 1
            if group_num == 1:
                return t
        
        return -1
    
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def find(self, node):
        if node == self.root[node]:
                return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, nodeX, nodeY):
        rootX = self.find(nodeX)
        rootY = self.find(nodeY)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
            
            return True
        
        return False