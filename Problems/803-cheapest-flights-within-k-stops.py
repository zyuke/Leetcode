# https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        G, C = {}, {}
        for f in flights:
            try:
                G[f[0]].append(f[1])
            except:
                G[f[0]] = [f[1]]
            
            C[(f[0], f[1])] = f[2]
            
        res = [0xffff]
        self.bfs(src, dst, K, G, C, 0, res)
        return res[0] if res[0] != 0xffff else -1
        # return res
    
    def bfs(self, cur_city, dest, K, G, C, cur_cost, res):
        if K >= -1:
            if cur_city == dest and cur_cost < res[0]:
                res[0] = cur_cost
            elif cur_city in G and cur_cost < res[0]:
                for next_city in G[cur_city]:
                    self.bfs(next_city, dest, K-1, G, C, cur_cost+C[(cur_city, next_city)], res)
                    
            