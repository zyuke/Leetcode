// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        sorted_dist = sorted(points, key = lambda x: x[0]*x[0]+x[1]*x[1])
        return sorted_dist[0:K]