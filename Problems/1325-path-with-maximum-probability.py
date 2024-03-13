# https://leetcode.com/problems/path-with-maximum-probability

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        visited = set()
        graph = {}

        for node in range(n):
            graph[node] = []
        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1], succProb[i]])
            graph[edges[i][1]].append([edges[i][0], succProb[i]])
        
        import heapq
        cur_pool = []
        heapq.heapify(cur_pool)
        heapq.heappush(cur_pool, [-1, start_node])
        res = [0]

        def search():
            if cur_pool:
                cur_node = heapq.heappop(cur_pool)
                visited.add(cur_node[1])
                if cur_node[1] == end_node:
                    res[0] = -1*cur_node[0]
                    return
                for next_node in graph[cur_node[1]]:
                    if next_node[0] not in visited:
                        heapq.heappush(cur_pool, [next_node[1]*cur_node[0], next_node[0]])
                search()
        
        search()
        return res[0]


        
