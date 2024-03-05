// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0],x[1]))
        max_d = -1
        res = 0

        for p in properties:
            if p[1] < max_d:
                res += 1
            else:
                max_d = p[1]
        
        return res