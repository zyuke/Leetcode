# https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        node_indegree = dict()
        graph = dict()
        for i in range(m):
            for j in range(n):
                node_indegree[(i,j)] = 0
                graph[(i,j)] = []
                
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        for i in range(m):
            for j in range(n):
                for d in directions:
                    new_i, new_j = i+d[0], j+d[1]
                    if 0<=new_i<=m-1 and 0<=new_j<=n-1:
                        if matrix[new_i][new_j] > matrix[i][j]:
                            graph[(i,j)].append((new_i,new_j))
                            node_indegree[(new_i,new_j)] += 1
        
        queue = []
        for i in range(m):
            for j in range(n):
                if node_indegree[(i,j)] == 0:
                    queue.append(((i,j),1))
                    
        res = 1
        seen = dict()
        
        while queue:
            node, l = queue.pop()
            # print(node,l)
            res = max(res, l)
            for next_node in graph[node]:
                try:
                    seen[next_node] = max(l, seen[next_node])
                except:
                    seen[next_node] = l
                node_indegree[next_node] -= 1
                if node_indegree[next_node] == 0:    
                    queue.append((next_node, seen[next_node]+1))
        
        return res
        
                                