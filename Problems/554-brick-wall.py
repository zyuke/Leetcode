# https://leetcode.com/problems/brick-wall

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        S = defaultdict(int)
        end = sum(wall[0])
        
        for row in wall:
            cum_sum = 0
            for b in row:
                cum_sum += b
                if cum_sum < end:
                    S[cum_sum] += 1
        
        max_count = 0
        for k in S:
            if S[k] > max_count:
                max_count = S[k]
        return len(wall) - max_count