# https://leetcode.com/problems/valid-square

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2:
            return False
        def is_valid(p1, p2, p3, p4):
            if -1*(p2[1]-p1[1])*(p4[1]-p3[1]) == (p2[0]-p1[0])*(p4[0]-p3[0]):
                if p1[0]+p2[0] == p3[0]+p4[0] and p1[1]+p2[1] == p3[1]+p4[1]:
                    if (p2[1]-p1[1])**2 + (p2[0]-p1[0])**2 == (p4[1]-p3[1])**2 + (p4[0]-p3[0])**2:
                        return True
            return False
        
        return is_valid(p1,p2,p3,p4) or is_valid(p1,p3,p2,p4) or is_valid(p1,p4,p2,p3)

        