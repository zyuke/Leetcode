// https://leetcode.com/problems/detect-squares

class DetectSquares:

    def __init__(self):
        self.p_count = {}

    def add(self, point: List[int]) -> None:
        p = (point[0],point[1])
        if p in self.p_count:
            self.p_count[p] += 1
        else:
            self.p_count[p] = 1

    def count(self, point: List[int]) -> int:
        res = 0
        p1 = (point[0], point[1])
        for p2 in self.p_count:
            if abs(p2[0]-p1[0]) == abs(p2[1] - p1[1]) and p2[0] != p1[0]:
                p3 = (p2[0],p1[1])
                p4 = (p1[0],p2[1])
                if p3 in self.p_count and p4 in self.p_count:
                    res += self.p_count[p2]*self.p_count[p3]*self.p_count[p4]
        
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)