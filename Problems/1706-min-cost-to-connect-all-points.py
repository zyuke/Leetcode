// https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [(0,0)]
        in_mst = [False]*n
        mst_cost = 0
        edges_used = 0
        
        while edges_used < n:
            w, cur_node = heapq.heappop(heap)
            if in_mst[cur_node]:
                continue
            
            in_mst[cur_node] = True
            mst_cost += w
            edges_used += 1
            
            for next_node in range(n):
                if not in_mst[next_node]:
                    next_w = abs(points[next_node][0]-points[cur_node][0]) + abs(points[next_node][1]-points[cur_node][1])
                    heapq.heappush(heap, (next_w, next_node))
            
        return mst_cost
            