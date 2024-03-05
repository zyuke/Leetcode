// https://leetcode.com/problems/count-all-possible-routes

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1]*(fuel + 1) for _ in range(len(locations))]
        N = 1000000007
        
        def search(cur_city, goal, cur_fuel):         
            if cur_fuel < 0:
                return 0
            if dp[cur_city][cur_fuel] != -1:
                return dp[cur_city][cur_fuel]

            count = 1 if cur_city == goal else 0
            for city in range(len(locations)):
                if city != cur_city:
                    count = (count + search(city, goal, cur_fuel - abs(locations[city] - locations[cur_city]))) % N
            dp[cur_city][cur_fuel] = count
            return count

        return search(start, finish, fuel)       
