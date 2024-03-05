// https://leetcode.com/problems/reconstruct-itinerary

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flightmap = {}
        for t in tickets:
            flightmap[t[0]] = []
            flightmap[t[1]] = []
        for t in tickets:
            flightmap[t[0]].append(t[1])
        
        visitmap = {}
        for start in flightmap:
            flightmap[start].sort()
            visitmap[start] = [False]*len(flightmap[start])
        
        n = len(tickets)
        self.res = []
        route = ['JFK']
        
        def backtrack(start, route):
            if len(route) == n+1:
                self.res = route
                return True
            for i, next_node in enumerate(flightmap[start]):
                if visitmap[start][i] == False:
                    visitmap[start][i] = True
                    found = backtrack(next_node, route+[next_node])
                    visitmap[start][i] = False
                    if found:
                        return True
            return False
        
        backtrack('JFK', route)
        return self.res
            