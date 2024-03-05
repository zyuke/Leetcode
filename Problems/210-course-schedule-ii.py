// https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph, indegree = defaultdict(list), {}
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
            
        zero_degree = [x for x in range(numCourses) if x not in indegree]
        res = []
        
        while zero_degree:
            v = zero_degree.pop(0)
            res.append(v)
            
            if graph[v]:
                for nxt in graph[v]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        zero_degree.append(nxt)
                    
        return res if len(res) == numCourses else []