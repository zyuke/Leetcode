import heapq

class MedianFinder:

    def __init__(self):
        self.L_heap = []
        self.R_heap = []
        heapq.heapify(self.L_heap)
        heapq.heapify(self.R_heap)
        self.L_size = 0
        self.R_size = 0
        

    def addNum(self, num: int) -> None:
        if self.L_size == self.R_size:
            if self.L_size == 0:
                heapq.heappush(self.R_heap, num)
            else:
                l = -1*self.L_heap[0]
                if num >= l:
                    heapq.heappush(self.R_heap, num)
                else:
                    l = heapq.heappushpop(self.L_heap, -1*num)
                    heapq.heappush(self.R_heap, -1*l) 
            self.R_size += 1
            return

        if self.L_size + 1 == self.R_size:
            r = self.R_heap[0]
            if num <= r:
                heapq.heappush(self.L_heap, -1*num)
            else:
                r = heapq.heappushpop(self.R_heap, num)
                heapq.heappush(self.L_heap, -1*r)
            self.L_size += 1
            return
        

    def findMedian(self) -> float:
        if self.L_size == self.R_size:
            return ((-1*self.L_heap[0] + self.R_heap[0]) / 2)
        if self.L_size + 1 == self.R_size:
            return self.R_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
