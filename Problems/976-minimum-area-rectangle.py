// https://leetcode.com/problems/minimum-area-rectangle

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set()
        for p in points:
            point_set.add((p[0],p[1]))
        
        res = math.inf
        exist = False
        
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2:
                    if (x2,y1) in point_set and (x1,y2) in point_set:
                        exist = True
                        area = abs(x1 -  x2) * abs(y1 - y2)
                                                  
                        res = min(res, area)
        
        return res if exist else 0