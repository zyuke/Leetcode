# https://leetcode.com/problems/destroying-asteroids

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        cur_mass = mass
        for a in asteroids:
            if cur_mass < a:
                return False
            else:
                cur_mass += a
        return True