// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {}
        for i in range(len(isConnected)):
            graph[i] = [i]
        for i in range(len(isConnected)):
            for j in range(i):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
               
        traversed = set()
        res = 0
        def search(x):
            traversed.add(x)
            for next_node in graph[x]:
                if not next_node in traversed:
                    search(next_node)
        
        for i in range(len(isConnected)):
            if i not in traversed:
                res += 1
                search(i)
        
        return res