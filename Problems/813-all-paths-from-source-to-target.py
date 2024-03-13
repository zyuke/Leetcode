# https://leetcode.com/problems/all-paths-from-source-to-target

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        end = len(graph)-1
        res = []
        def dfs(node, prev):
            if node == end:
                res.append(prev+[node])
                return
            for i in graph[node]:
                dfs(i, prev+[node])
                
        dfs(0, [])
        return res