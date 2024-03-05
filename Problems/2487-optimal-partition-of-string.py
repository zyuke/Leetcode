// https://leetcode.com/problems/optimal-partition-of-string

class Solution:
    def partitionString(self, s: str) -> int:
        cur_map = set()
        ct = 1
        for c in s:
            if c not in cur_map:
                cur_map.add(c)
            else:
                ct += 1
                cur_map = set()
                cur_map.add(c)
        return ct