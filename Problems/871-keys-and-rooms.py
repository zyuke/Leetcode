// https://leetcode.com/problems/keys-and-rooms

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        room_status = [0 for i in range(N)]
        room_status[0] = 1
        
        def dfs(room):
            for k in room:
                if room_status[k] == 0:
                    room_status[k] = 1
                    dfs(rooms[k])

                    
        dfs(rooms[0])
        
        return room_status == [1 for i in range(N)]