# https://leetcode.com/problems/design-hit-counter

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = [[0, i+1] for i in range(300)]
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = (timestamp-1) % 300
        if self.counter[idx][1] == timestamp:
            self.counter[idx][0] += 1
        else:
            self.counter[idx][0] = 1
            self.counter[idx][1] = timestamp
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        for count in self.counter:
            if timestamp - count[1] < 300:
                res += count[0]
        return res
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)