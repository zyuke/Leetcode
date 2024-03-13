# https://leetcode.com/problems/lemonade-change

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        tracking = [0, 0]
        for i in bills:
            if i == 5:
                tracking[0] += 1
            elif i == 10:
                tracking[1] += 1
                tracking[0] -= 1
            elif i == 20:
                if tracking[1] >= 1:
                    tracking[1] -= 1
                    tracking[0] -= 1
                else:
                    tracking[0] -= 3
            if tracking[0] < 0 or tracking[1] < 0:
                return False
        return True