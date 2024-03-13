# https://leetcode.com/problems/asteroid-collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        res = []
        
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                temp = a
                while len(stack) > 0:
                    if stack[-1] < abs(a):
                        stack.pop(-1)
                    elif stack[-1] == abs(a):
                        stack.pop(-1)
                        temp = None
                        break
                    else:
                        break
                if len(stack) == 0 and temp != None:
                    res.append(temp)
                    
        return res + stack