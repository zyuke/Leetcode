// https://leetcode.com/problems/queue-reconstruction-by-height

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        sort_people = sorted(people, key = lambda x: (-x[0], x[1]))
        for p in sort_people:
            res.insert(p[1], p)
        
        return res