# https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph, self.temp, self.perm = {}, {}, {}
        self.res = True
        
        for i in range(numCourses):
            self.graph[i] = []
            self.temp[i] = False
            self.perm[i] = False
            
        for pair in prerequisites:
            self.graph[pair[1]].append(pair[0])
        
        self.all_classes = list(range(numCourses))
            
        def dfs(node):
            if self.perm[node] == True:
                return
            if self.temp[node] == True:
                self.res = False
                return
            self.temp[node] = True
            for next_node in self.graph[node]:
                dfs(next_node)
            self.temp[node] = False
            self.perm[node] = True
            self.all_classes.remove(node)
            
        while len(self.all_classes) > 0 and self.res:
            dfs(self.all_classes[0])
            
        return self.res
            
            
        