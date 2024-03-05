// https://leetcode.com/problems/maximum-score-of-a-node-sequence

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = {}
        for i in range(len(scores)):
            graph[i] = []
        for x, y in edges:
            graph[x].append([scores[y], y])
            graph[y].append([scores[x], x])
        
        for i in range(len(scores)):
            graph[i] = heapq.nlargest(3, graph[i])
        
        res = -1
        for x, y in edges:
            for sz, z in graph[x]:
                if z != y:
                    for sw, w in graph[y]:
                        if w != x and w != z:
                            s = scores[x]+scores[y]+sz+sw
                            res = max(res, s)
        
        return res