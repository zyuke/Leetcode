// https://leetcode.com/problems/time-needed-to-inform-all-employees

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        time_to_head = {headID: informTime[headID]}
        self.res = 0
        
        def search(employee):
            if employee in time_to_head:
                return time_to_head[employee]
            time_to_head[employee] = search(manager[employee]) + informTime[employee]
            self.res = max(self.res, time_to_head[employee])
            return time_to_head[employee]
        
        for i in range(n):
            if i not in time_to_head:
                search(i)
        
        return self.res