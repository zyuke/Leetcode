# https://leetcode.com/problems/evaluate-division

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = dict()
        edge2value = dict()
        
        for i in range(len(equations)):
            x, y = equations[i]
            if x in graph:
                graph[x].append(y)
            else:
                graph[x] = [y]
            if y in graph:
                graph[y].append(x)
            else:
                graph[y] = [x]
            edge2value[(x,y)] = values[i]
            edge2value[(y,x)] = 1/values[i]
        
        res = []
        # print(graph)
        def search(start, dest):
            if (start not in graph) or (dest not in graph):
                return -1.0
            if start == dest:
                return 1.0
            queue = [(start, 1.0)]
            traversed = set()
            while queue:
                cur_node, v = queue.pop()
                if cur_node == dest:
                    return v
                traversed.add(cur_node)
                if cur_node in graph:
                    for next_node in graph[cur_node]:
                        if next_node not in traversed:
                            queue.append((next_node, v*edge2value[(cur_node, next_node)]))
            
            return -1
        
        for q in queries:
            res.append(search(q[0], q[1]))
        
        return res
                            