from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        for i in range(int(sqrt(c)) + 1):
            squares.add(i*i)
        for j in squares:
            if c-j in squares:
                return True
        return False
        
